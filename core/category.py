from config import get_config

from bs4 import BeautifulSoup

from utils.json import JSONSerializer
from utils.dirs import DIRMaker
from utils.client import HTTPXClient

import asyncio


class BaseParser:
    config = get_config()


class AsyncParser(BaseParser):
    async def parse_category(self, cat: str, subcats: list[str]) -> None:
        cat_names = await JSONSerializer.look(self.config.CAT_NAMES)

        dir_path = await DIRMaker.create(cat_names[cat])

        tasks = [
            asyncio.create_task(self.parse_subcategory(subcat, dir_path))
            for subcat in subcats
        ]
        print(self.parse_category, len(tasks))

        await asyncio.gather(*tasks)


    async def parse_subcategory(self, subcat: str, dir_path: str) -> None:

        link = self.config.STATIC_RQ_LINK.replace("{category}", subcat)

        async with await HTTPXClient() as client:
            response = await client.request("GET", url=link)
            
            products = response.json()["moreProducts"]["productWindow"]

            tasks = [asyncio.to_thread(self.parse_page(product["pipUrl"], dir_path)) for product in products]
            print(len(tasks))
            await asyncio.gather(*tasks)
 

    async def parse_page(self, link: str, dir_path: str) -> None:
        async with await HTTPXClient() as client:
            response = await client.request("GET", url=link)
            


class SyncParser(BaseParser):
    pass
