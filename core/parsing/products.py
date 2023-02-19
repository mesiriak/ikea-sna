import asyncio
from typing import Any

from bs4 import BeautifulSoup

import config
from utils.client import CustomClient


async def parse_page(subcat: str) -> list[dict[str, Any]]:
    """
    Getting all products from subcategory and returns parsed list of them

    Args:
        subcat (str): name of subcategory, on which will be made http request
    Returns:
        list[dict[str, Any]]: list of parsed products
    """

    link = config.STATIC_RQ_LINK.replace("{category}", subcat)

    async with CustomClient() as client:
        response = await client.get(link, follow_redirects=True)

    products_list = response.json()["moreProducts"]["productWindow"]

    products_tasks = [
        parse_product(link=product["pipUrl"]) for product in products_list
    ]

    summary = []

    async with asyncio.Semaphore(config.SEMAPHORE_LIMIT):
        for task in products_tasks:
            page_results = await asyncio.create_task(task)
            summary.append(page_results)

    return summary


async def parse_product(link: str) -> dict[str, Any]:
    async with CustomClient() as client:
        response = await client.get(link, follow_redirects=True, timeout=10)

    scrapper = BeautifulSoup(response.text, "lxml")

    # make parse logic here

    title = scrapper.find("h1", class_="pip-header-section").text
    code = scrapper.find("span", class_="pip-product-identifier__value").text
    price = (
        scrapper.find("span", class_="pip-temp-price__integer")
        .text.split(",")[0]
        .replace(" ", "")
    )
    description = scrapper.find("div", class_="pip-product-details__container").text

    imgs_grid = scrapper.find("div", class_="pip-media-grid__grid")
    imgs = [
        image["src"].replace("f=s", "f=xxl")
        for image in imgs_grid.find_all("img", class_="pip-image")
    ]

    qualities_container = scrapper.find(
        "div", class_="pip-product-dimensions__dimensions-container"
    )
    qualities = [
        item.text.replace("\xa0", " ").split(": ")
        for item in qualities_container.find_all(
            "p", class_="pip-product-dimensions__measurement-wrapper"
        )
    ]

    product = {
        "title": title,
        "ru_title": "",
        "code": code,
        "price": int(price) * config.EXCHANGE_RATE,
        "description": description,
        "ru_description": "",
        "imgs": imgs,
        "qualities": qualities,
    }

    return product
