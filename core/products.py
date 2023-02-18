import asyncio
from typing import Any

from bs4 import BeautifulSoup

import config
from utils.client import CustomClient


async def parse_page(subcat: str) -> None:
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

    async with asyncio.Semaphore(config.SEMAPHORE_LIMIT):
        for task in products_tasks:
            asyncio.create_task(task)


async def parse_product(link: str) -> dict[str, Any]:
    async with CustomClient() as client:
        response = await client.get(link, follow_redirects=True, timeout=10)

    scrapper = BeautifulSoup(response.text, "lxml")

    # make parse logic here

    product = {
        "title": "",
        "ru_title": "",
        "code": "",
        "price": "",
        "description": "",
        "ru_description": "",
        "imgs": "",
        "qualities": "",
    }

    return product
