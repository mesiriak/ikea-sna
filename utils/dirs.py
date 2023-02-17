import os
import shutil

from config import get_config

config = get_config()


def output_checker() -> str:
    if not os.path.exists(config.OUTPUT_DIR):
        os.mkdir(config.OUTPUT_DIR)

    return config.OUTPUT_DIR


def create_dir(name: str, custom=False) -> str:

    if custom:
        os.mkdir(name)
        return name

    path = os.path.join(config.OUTPUT_DIR, name)
    os.mkdir(path)

    return path


def output_delete() -> None:
    for files in os.listdir(config.OUTPUT_DIR):
        path = os.path.join(config.OUTPUT_DIR, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
