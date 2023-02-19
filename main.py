from core.sessions import AsyncParseSession


def main() -> None:
    session = AsyncParseSession()

    session()


if __name__ == "__main__":
    main()
