import json
import os

from typing import Any


def save(data: list[dict[str, Any]], path: str, name: str = None) -> None:
    """Creating json file with last directory name if name parameter doesn't exist"""

    if name:
        path = path + "/" + name
    else:
        path = path + "/" + path.split("/")[-1] + ".json"

    preload = []

    if os.path.exists(path):
        preload = json.load(open("products.json", "r", encoding="utf-8"))

    with open("products.json", "w", encoding="utf-8") as file:
        preload.extend(data)
        json.dump(preload, file, indent="\t", ensure_ascii=False)

    return None
