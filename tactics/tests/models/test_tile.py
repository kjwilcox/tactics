from flexmock import flexmock

from tactics.models import tile as module


def mock_loader():
    flexmock(module).should_receive(
        'loader.load_image'
    ).and_return(
        flexmock()
    )


def test_grass_tile_does_not_raise():
    mock_loader()
    module.GrassTile()


def test_water_tile_does_not_raise():
    mock_loader()
    module.WaterTile()
