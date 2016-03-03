import flexmock

from tactics import main as module


def test_update_does_not_raise():
    module.update(1)


def test_main_does_not_raise():
    flexmock(
        module,
        pyglet=flexmock(window=flexmock(Window=flexmock(
            event=lambda: None,
        )))
    )

    flexmock(module).should_receive('pyglet.clock.ClockDisplay')
    flexmock(module).should_receive('pyglet.clock.schedule_interval')
    flexmock(module).should_receive('pyglet.app.run')

    module.main()