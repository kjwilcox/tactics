import functools

import pyglet

from tactics import config


@functools.lru_cache()
def get_loader():
    loader = pyglet.resource.Loader(config.RESOURCE_PATHS)
    loader.reindex()

    return loader


def load_image(path):
    return get_loader().image(path)
