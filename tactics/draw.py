import pyglet

from tactics.window import get_window


_fps_display = None


def on_draw():
    """ Draw screen. """
    get_window().clear()

    global _fps_display
    if not _fps_display:
        _fps_display = pyglet.clock.ClockDisplay()

    _fps_display.draw()
