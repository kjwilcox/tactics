from tactics.models import tilemap as module

from flexmock import flexmock


def test_tilemap_creation_and_draw_does_not_raise():
    flexmock(module).should_receive(
        'multimedia.SpriteBatch'
    ).and_return(flexmock(draw=lambda: None))

    flexmock(module).should_receive(
        'multimedia.Sprite'
    ).and_return(flexmock())

    tile = module.TileMap(2, 2, 16)
    tile.draw()


