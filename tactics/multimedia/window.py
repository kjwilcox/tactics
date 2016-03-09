import functools

import pyglet

from tactics import config


def create_window():
    """
    :return: pyglet window
    """
    return pyglet.window.Window(
        config.MAP_SIZE.x * config.TILE_SIZE,
        config.MAP_SIZE.y * config.TILE_SIZE,
    )


@functools.lru_cache
def get_window():
    """
    :return: pyglet window.
    """
    return create_window()

