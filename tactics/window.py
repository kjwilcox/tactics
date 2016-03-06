import pyglet
import pyrsistent

_window = None

TILE_SIZE = 16
MAP_SIZE = pyrsistent.m(x=32, y=18)


def create_window():
    """
    :return: pyglet window
    """
    return pyglet.window.Window(MAP_SIZE.x * TILE_SIZE, MAP_SIZE.y * TILE_SIZE)


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
