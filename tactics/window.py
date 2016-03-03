import pyglet


_window = None


def get_window():
    """
    :return: Main pyglet game window.
    """
    global _window
    if not _window:
        _window = pyglet.window.Window()
    return _window
