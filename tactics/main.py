import pyglet

from .draw import on_draw
from .update import update
from .window import get_window

TARGET_FRAMERATE = 60
TICK_RATE = 1 / TARGET_FRAMERATE  # Frame time, in seconds


def main():
    # Register draw handler
    get_window().event(on_draw)

    # Register game state update logic
    pyglet.clock.schedule_interval(update, TICK_RATE)

    pyglet.app.run()


if __name__ == "__main__":
    main()
