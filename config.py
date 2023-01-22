from pydantic import BaseSettings
from functools import lru_cache

class Config(BaseSettings):
    

    # True - if parser should work in async mode, False - otherwise
    ASYNC: bool = True

    # True - if async translation, False - if sync
    TRANSLATION_MODE: bool = True

    class Config:
        env_file = ".env"


@lru_cache()
def get_config() -> Config:
    return Config()