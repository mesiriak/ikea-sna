from config import get_config

from httpx import AsyncClient, Client


class HTTPXClient:
    async def _get_async_client() -> AsyncClient:
        return AsyncClient()

    async def _get_sync_client() -> Client:
        return Client()

    def __new__(self) -> AsyncClient | Client:
        config = get_config()

        if config.ASYNC == True:
            return self._get_async_client()

        return self._get_sync_client()
