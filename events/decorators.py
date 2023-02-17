from utils.dirs import output_checker, output_delete


def on_startup(func):
    output_checker()
    output_delete()

    return func

