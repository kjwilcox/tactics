from tactics import config
from tactics.models import battle, tilemap

_battle = None


def get_battle():
    global _battle
    if not _battle:
        _battle = battle.Battle(
            _map=tilemap.TileMap(
                config.MAP_SIZE.x,
                config.MAP_SIZE.y,
                config.TILE_SIZE
            ),
            teams=None,
        )
    return _battle


