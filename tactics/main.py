import pyglet

TARGET_FRAMERATE = 60
TICK_RATE = 1 / TARGET_FRAMERATE  # Frame time, in seconds


def update(dt):
    """
    Performs the game state simulation.
    :param dt: Time in seconds since last update.
    """
    pass


def main():
    window = pyglet.window.Window()

    fps_display = pyglet.clock.ClockDisplay()

    @window.event
    def on_draw():
        """ Draw screen. """
        window.clear()
        fps_display.draw()

    # Register game state update logic
    pyglet.clock.schedule_interval(update, TICK_RATE)

    pyglet.app.run()


if __name__ == "__main__":
    main()
