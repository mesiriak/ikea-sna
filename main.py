from core.sessions import AsyncSession


def main() -> None:
    session = AsyncSession()

    session()


if __name__ == "__main__":
    main()
