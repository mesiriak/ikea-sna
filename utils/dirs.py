import os, shutil

class DIRMaker:
    @staticmethod
    async def create() -> str:
        pass
    
    @staticmethod
    async def clear() -> str:
        for dirpath in os.walk("output/"):
            shutil.rmtree(dirpath)
