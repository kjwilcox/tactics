from tactics.models import tilemap as module

from flexmock import flexmock


def test_tilemap_creation_and_draw_does_not_raise():
    mock_tile = flexmock(image=flexmock())
    flexmock(module).should_receive(
        'tile.GrassTile'
    ).and_return(mock_tile)
    flexmock(module).should_receive(
        'tile.WaterTile'
    ).and_return(mock_tile)

    flexmock(module).should_receive(
        'multimedia.SpriteBatch'
    ).and_return(flexmock(draw=lambda: None))

    flexmock(module).should_receive(
        'multimedia.Sprite'
    ).and_return(flexmock())

    tile = module.TileMap(2, 2, 16)
    tile.draw()


