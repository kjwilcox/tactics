from tactics import tilemap

_map = None


def get_map():
    global _map
    if not _map:
        _map = tilemap.TileMap(32, 18, 16)

    return _map
