from tactics import config as module


def test_tile_size_has_not_changed():
    assert module.TILE_SIZE == 16
