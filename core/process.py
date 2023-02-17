import asyncio

import uvloop

from config import get_config
from core.parsers import SyncParser, AsyncParser
from utils.json import load_json


class BaseProcess:

    config = get_config()


class SyncProcess(BaseProcess):
    def start_process(self):
        return NotImplemented

    def __call__(self, *args, **kwargs):
        self.sync_parser = SyncParser()
        self.start_process()


class AsyncProcess(BaseProcess):
    async def start_process(self):
        cats = load_json(self.config.CAT_NAMES)

        cats_to_parse = [
            asyncio.create_task(
                self.async_parser.parse_category(cat=cat, cat_name=cat_name)
            )
            for cat, cat_name in cats.items()
        ]

        await asyncio.gather(*cats_to_parse)

    async def __call__(self):
        self.async_parser = await AsyncParser.create_parser()
        await self.start_process()
