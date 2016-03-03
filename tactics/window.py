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
    if not _window:
        _window = create_window()
    return _window
