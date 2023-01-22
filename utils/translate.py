from config import get_config


class AsyncTranslator:

    pass


class SyncTranslator:

    pass


async def get_translator():
    config = get_config()

    if config.TRANSLATION_MODE == True:
        return AsyncTranslator()
    
    return SyncTranslator()
    