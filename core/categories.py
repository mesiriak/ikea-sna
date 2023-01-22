from config import get_config

from core.category import AsyncParser, SyncParser

from utils.json import JSONSerializer
from utils.client import HTTPXClient

import asyncio


class _BaseSession:
    config = get_config()
    parser = None


class _AsyncSession(_BaseSession):

    parser = AsyncParser()

    async def parse_categories(self):
        cats_preload = await JSONSerializer.look(self.config.CAT_FILE)

        cats = [
            asyncio.create_task(self.parser.parse_category(cat=cat, subcats=subcats))
            for cat, subcats in cats_preload.items()
        ]

        await asyncio.gather(*cats)

    async def __call__(self):

        await self.parse_categories()


class _SyncSession(_BaseSession):

    parser = SyncParser()

    def __call__(self) -> None:
        pass


class Session:
    def __new__(self) -> _AsyncSession | _SyncSession:
        config = get_config()
        if config.ASYNC == True:
            return _AsyncSession()
        return _SyncSession()
