import os

import config


def create_dir(name: str, source: str = config.OUTPUT_DIR) -> str:
    path = source + "/" + name
    os.mkdir(path)

    return path
