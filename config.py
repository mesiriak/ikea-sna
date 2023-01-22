from pydantic import BaseSettings
from functools import lru_cache


class Config(BaseSettings):

    # True - if parser should work in async mode, False - otherwise
    ASYNC: bool = True

    # True - if async translation, False - if sync
    TRANSLATION_MODE: bool = True

    # IKEA api link
    STATIC_RQ_LINK: str = "https://sik.search.blue.cdtapps.com/pl/pl/product-list-page/more-products?category={category}&start=0&end=6666666"

    # categories .json file
    CAT_FILE: str = "cats.json"

    # categories names .json file
    CAT_NAMES: str = "catnames.json"

    class Config:
        env_file = ".env"


@lru_cache()
def get_config() -> Config:
    return Config()
