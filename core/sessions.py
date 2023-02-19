import asyncio

from core.parsing.categories import parse_cats


class AsyncParseSession:
    # loop = uvloop.new_event_loop()
    # asyncio.set_event_loop(loop)

    def __call__(self) -> None:
        asyncio.run(parse_cats())
