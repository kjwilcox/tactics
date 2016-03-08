import pyglet

from tactics import config

_window = None


def create_window():
    """
    :return: pyglet window
    """
    return pyglet.window.Window(
        config.MAP_SIZE.x * config.TILE_SIZE,
        config.MAP_SIZE.y * config.TILE_SIZE,
    )


def get_window():
    """
    :return: pyglet window.
    """
    global _window
    if _window:
        return _window

    window = create_window()
    _window = window
    return window
