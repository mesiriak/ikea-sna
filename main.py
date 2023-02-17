import asyncio

import uvloop

from config import get_config
from core.process import AsyncProcess, SyncProcess
from events.decorators import on_startup


@on_startup
async def main():
    config = get_config()
    if config.ASYNC is True:
        session = AsyncProcess()
        await session()
    else:
        session = SyncProcess()
        session()


if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main())
