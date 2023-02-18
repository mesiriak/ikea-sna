import time
from typing import Any

import config
from convertors.json_conv import load
from core.products import parse_page


async def parse_cats(source: str = "catnames.json") -> None:
    """
    Categories - just symbolic name for group of real categories,
    which I call 'subcategories' in this project

    **Sham-sync now

    Args:
        source (str): path to cat - names file
    """

    cats = load(source)

    # dir creating should be pasted here

    for cat in cats:
        await parse_subcats(cat=cat, path=config.OUTPUT_DIR + cats[cat])


async def parse_subcats(cat: str, path: str, source: str = "cats.json") -> None:
    """
    Proxying work on parse_page func

    **Sham-sync now

    Args:
        cat (str): name of category
        path (str): place where subcat file will be saved
        source (str): path to cats - subcats file
    Returns:
        list[dict[str, Any]]: list of all products in subcategory
    """
    subcats = load(source)[cat]

    products = []

    # dir creating should be pasted here also

    for subcat in subcats:
        products += await parse_page(subcat=subcat)

    # save to json in created dir here
