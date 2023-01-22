import asyncio


async def main() -> None:
    from utils.json import JSONSerializer

    file = await JSONSerializer.look("cats.json")

    for item, value in file.items():
        print(f'\"{item}\": \"\",') 


if __name__ == "__main__":
    asyncio.run(main())
