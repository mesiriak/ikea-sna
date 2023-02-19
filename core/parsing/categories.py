import config
from convertors.json_conv import load, save
from core.parsing.products import parse_page
from utils.dirs import create_dir


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
        print(f"Category - {cat}, working...")
        cat_path = create_dir(name=cats[cat])
        await parse_subcats(cat=cat, path=cat_path)
        print(f"Category - {cat}, finished")


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

    for subcat in subcats:
        subcat_path = create_dir(name=subcat, source=path)
        print(f"{cat} - subcategory {subcat} parsing")
        subcat_results = await parse_page(subcat=subcat)
        # asyncio.create_task(parse_page(subcat=subcat))
        save(data=subcat_results, path=subcat_path, name="products")
        print(f"{cat} - subcategory {subcat} ready")
