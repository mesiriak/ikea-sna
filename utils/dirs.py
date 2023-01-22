import os, shutil


class DIRMaker:
    @staticmethod
    async def create(name: str) -> str:
        path = os.path.join("output", name)
        print(path)
        os.mkdir(path)
        return path

    @staticmethod
    def delete_output() -> None:
        for files in os.listdir("output"):
            path = os.path.join("output", files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)
