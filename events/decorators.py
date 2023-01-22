from utils.dirs import DIRMaker


def pre_start(func):

    DIRMaker.delete_output()
    return func
