from flexmock import flexmock

from tactics.models import unit as module


def test_unit_draw_does_not_raise():
    mock_drawable = flexmock(draw=lambda: None)
    flexmock(module).should_receive(
        'multimedia.Sprite'
    ).and_return(mock_drawable)

    unit = module.Unit(
        image=flexmock(),
        position=module.vector.Vector2(1, 1),
        stats=None,
    )
    unit.draw()
