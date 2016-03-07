from flexmock import flexmock

from tactics.models import team as module


def test_team_draw_does_not_raise():
    mock_drawable = flexmock(draw=lambda: None)
    battle = module.Team(
        units=[mock_drawable, mock_drawable],
        controller=None
    )
    battle.draw()
