import os.path
from typing import Any

import asyncio

import config
from convertors.json_conv import load, save
from utils.translators import CustomTranslator


async def translate_file(path: str) -> None:
    products_data = load(path)

    products_tasks = [translate_product(item) for item in products_data]

    summary = []

    async with asyncio.Semaphore(config.SEMAPHORE_TRANSLATION_LIMIT):
        for task in products_tasks:
            summary += await asyncio.create_task(task)

    save(data=summary, path=os.path.dirname(path), name="translated")


async def translate_product(data: dict[str, Any]) -> dict[str, Any]:

    title = await CustomTranslator.to_uk(data["title"]) if data["title"] != "" else ""
    ru_title = await CustomTranslator.to_ru(data["title"]) if data["title"] != "" else ""

    description = await CustomTranslator.to_uk(data["description"]) if data["description"] != "" else ""
    ru_description = await CustomTranslator.to_ru(data["description"]) if data["description"] != "" else ""

    qualities = [
        [await CustomTranslator.to_uk(item[0]),
         await CustomTranslator.to_uk(item[1])]
        for item in data["qualities"]
    ]

    product = {
        "title": title,
        "ru_title": ru_title,
        "code": data["code"],
        "price": "{:.2f}".format(data["price"]),
        "description": description,
        "ru_description": ru_description,
        "imgs": data["imgs"],
        "qualities": qualities,
    }

    return product


if __name__ == "__main__":
    # asyncio.run(translate_file(path))
    pass
