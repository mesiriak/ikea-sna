from config import get_config

from httpx imprt AsyncClient, Client


class HTTPXClient:

    @staticmethod
    async def _get_async_client() -> AsyncClient:
        return AsyncClient()

    @staticmethod
    async def _get_sync_client() -> Client:
        return Client()

    @staticmethod
    async def get_client() -> AsyncClient | Client:
        config = get_config()

        if config.ASYNC == True:
            return _get_async_client()

        return _get_sync_client()