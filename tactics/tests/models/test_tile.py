from flexmock import flexmock

from tactics.models import tile as module


def mock_loader():
    flexmock(module).should_receive(
        'loader.get_loader'
    ).and_return(
        flexmock(
            image=lambda name: None
        )
    )


def test_grass_tile_does_not_raise():
    module.GrassTile()


def test_water_tile_does_not_raise():
    module.WaterTile()
