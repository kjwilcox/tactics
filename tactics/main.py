import pyglet

from tactics import config
from tactics.draw import on_draw
from tactics.update import update
from tactics.window import get_window


def main():
    # Register draw handler
    get_window().event(on_draw)

    # Register game state update logic
    pyglet.clock.schedule_interval(update, config.TICK_RATE)

    pyglet.app.run()


if __name__ == "__main__":
    main()
