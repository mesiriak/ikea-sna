from config import get_config

from utils.json import JSONSerializer
from utils.client import HTTPXClient

import asyncio

class _BaseSession:
    config = get_config()

class _AsyncSession(_BaseSession):
    async def parse_categories(self):
        cats_preload = await JSONSerializer.look(self.config.CAT_FILE)

        # create asyncio tasks which will contain every category  
        cats = [asyncio.create_task(

        ) for cat, value in cats_preload.items()]

    def __call__():
        # have to call Session() and start the proccess
        pass


class _SyncSession(_BaseSession):
    pass


class Session:
    def __new__() -> _AsyncSession | _SyncSession:
        config = get_config()
        if config.ASYNC == True:
            return _AsyncSession()
        return _SyncSession()
