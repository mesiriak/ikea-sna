from config import get_config

from gpytranslate import Translator
from gpytranslate import SyncTranslator as STranslator


class BaseTranslator:
    _TRANSLATOR_INSTANCE = None


class AsyncTranslator(BaseTranslator):

    _TRANSLATOR_INSTANCE = Translator()

    async def pl_to_ua(self, text: str) -> str:
        translation = await self._TRANSLATOR_INSTANCE.translate(
            text=text, sourcelang="pl", targetlang="uk"
        )
        return translation.text

    async def pl_to_ru(self, text: str) -> str:
        translation = await self._TRANSLATOR_INSTANCE.translate(
            text=text, sourcelang="pl", targetlang="ru"
        )
        return translation.text


class SyncTranslator(BaseTranslator):

    _TRANSLATOR_INSTANCE = STranslator()

    def pl_to_ua(self, text: str) -> str:
        translation = self._TRANSLATOR_INSTANCE.translate(
            text=text, sourcelang="pl", targetlang="uk"
        )
        return translation.text

    def pl_to_ru(self, text: str) -> str:
        translation = self._TRANSLATOR_INSTANCE.translate(
            text=text, sourcelang="pl", targetlang="ru"
        )
        return translation.text


def get_translator() -> AsyncTranslator | SyncTranslator:
    config = get_config()

    if config.TRANSLATION_MODE == True:
        return AsyncTranslator()

    return SyncTranslator()
