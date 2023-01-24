from events.decorators import pre_start
from core.categories import Session

import asyncio

import time

@pre_start
async def main() -> None:


    t1 = time.time()
    session = Session()

    await session()
    t2 = time.time() - t1

    print(t2)

if __name__ == "__main__":
    asyncio.run(main())
