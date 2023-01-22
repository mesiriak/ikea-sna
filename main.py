from events.decorators import pre_start
from core.categories import Session

import asyncio


@pre_start
async def main() -> None:

    session = Session()

    await session()


if __name__ == "__main__":
    asyncio.run(main())
