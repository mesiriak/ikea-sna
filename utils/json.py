import json


class JSONSerializer:
    @staticmethod
    async def look(file_name: str) -> str:
        file_text = json.load(open(file_name, "r", encoding="utf-8"))

        return file_text

    @staticmethod
    async def save() -> bool:
        pass

    @staticmethod
    async def create() -> str:
        pass
