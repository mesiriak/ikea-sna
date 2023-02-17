import asyncio
import os.path
import random
from typing import Any

from config import get_config
from utils.client import SyncRqClient, AsyncRqClient
from utils.dirs import create_dir
from utils.json import load_json


class BaseParser:
    config = get_config()


class SyncParser(BaseParser):

    sync_client = SyncRqClient().get_client()

    def parse_category(self, cat, cat_name):
        pass

    def parse_subcategory(self, sub_cat, path):
        pass

    def parse_page(self, link):
        pass


class AsyncParser(BaseParser):
    def __init__(self):
        self.async_client = None

    @classmethod
    async def create_parser(cls):
        self = cls()
        self.async_client = await AsyncRqClient().get_client()
        return self

    async def parse_category(self, cat, cat_name):

        sub_cats = load_json(self.config.CAT_FILE)
        cat_path = create_dir(cat_name)

        sub_cats_to_parse = [
            asyncio.create_task(self.parse_subcategory(sub_cat=sub_cat, path=cat_path))
            for sub_cat in sub_cats[cat]
        ]

        await asyncio.gather(*sub_cats_to_parse)

    async def parse_subcategory(self, sub_cat, path):
        link = self.config.STATIC_RQ_LINK.replace("{category}", sub_cat)
        sub_cat_path = create_dir(path + "/" + sub_cat, custom=True)

        response = await self.async_client.get(url=link)

        products = response.json()["moreProducts"]["productWindow"]

        products_to_parse = [
            asyncio.create_task(self.parse_page(product["pipUrl"])) for product in products
        ]

        parsed_products = await asyncio.gather(*products_to_parse)

    async def parse_page(self, link: str) -> dict[str, Any]:

        res = await self.async_client.get(url=link)

        print(link)
