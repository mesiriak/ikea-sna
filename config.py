# True - if parser should work in async mode, False - otherwise
ASYNC: bool = True

# True - if async translation, False - if sync
TRANSLATION_MODE: bool = True

# IKEA api link
STATIC_RQ_LINK: str = (
    "https://sik.search.blue.cdtapps.com/pl/pl/product-list-page/more-products?category={"
    "category}&start=0&end=6666666"
)

# categories .json file
CAT_FILE: str = "cats.json"

# categories names .json file
CAT_NAMES: str = "catnames.json"

# path to directory with results
OUTPUT_DIR: str = "output/"

# uah\pl multiplier
EXCHANGE_RATE = 15

# max tasks running in same time
SEMAPHORE_LIMIT: int = 100
SEMAPHORE_TRANSLATION_LIMIT: int = 100
