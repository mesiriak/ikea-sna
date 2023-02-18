# True - if parser should work in async mode, False - otherwise
ASYNC: bool = True

# True - if async translation, False - if sync
TRANSLATION_MODE: bool = True

# IKEA api link
STATIC_RQ_LINK: str = "https://sik.search.blue.cdtapps.com/pl/pl/product-list-page/more-products?category={" \
                      "category}&start=0&end=6666666"

# categories .json file
CAT_FILE: str = "cats.json"

# categories names .json file
CAT_NAMES: str = "catnames.json"

OUTPUT_DIR: str = "output/"

SEMAPHORE_LIMIT: int = 100
