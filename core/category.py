from config import get_config

from utils.json import JSONSerializer
from utils.dirs import DIRMaker

class BaseParser:
    config = get_config()

class AsyncParser(BaseParser):
    async def parse_category(self, cat: str, value: list[str]) -> None:
        cat_names = await JSONSerializer.look(self.config.CAT_NAMES)
        
        # have to create dirs with subcategories name
        await DIRMaker.create()

        # have to start parsing subcategories


class SyncParser(BaseParser):
    pass
