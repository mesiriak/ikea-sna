from httpx import Client, AsyncClient, Limits


class BaseClient:
    limits = Limits(max_connections=None, max_keepalive_connections=None)


class AsyncRqClient(BaseClient):
    async def get_client(self) -> AsyncClient:

        return AsyncClient(limits=self.limits)


class SyncRqClient(BaseClient):
    def get_client(self) -> Client:

        return Client(limits=self.limits)
