import pyglet


_window = None


def create_window():
    """
    :return: pyglet window
    """
    return pyglet.window.Window()


def get_window():
    """
    :return: Main pyglet game window.
    """
    global _window
    if _window:
        return _window

    window = create_window()
    _window = window
    return window
