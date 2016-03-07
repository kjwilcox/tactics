from tactics import config
from tactics import tilemap

_map = None


def get_map():
    global _map
    if not _map:
        _map = tilemap.TileMap(config.MAP_SIZE.x, config.MAP_SIZE.y, config.TILE_SIZE)
    return _map
