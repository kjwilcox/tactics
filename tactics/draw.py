import pyglet

from tactics import game_map
from tactics.window import get_window


fps_counter = pyglet.clock.ClockDisplay()


def draw_fps_counter():
    fps_counter.draw()


def clear_screen():
    get_window().clear()


def on_draw():
    """ Draw screen. """

    clear_screen()

    game_map.get_map().draw()

    draw_fps_counter()
