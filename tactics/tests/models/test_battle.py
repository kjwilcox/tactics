from flexmock import flexmock

from tactics.models import battle as module


def test_battle_draw_does_not_raise():
    mock_drawable = flexmock(draw=lambda: None)
    battle = module.Battle(mock_drawable, mock_drawable)
    battle.draw()
