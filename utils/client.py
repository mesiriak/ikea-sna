from httpx import AsyncClient


class CustomClient:
    def __new__(cls) -> AsyncClient:
        return AsyncClient()
