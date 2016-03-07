

from tactics import config
from tactics import loader
from tactics.models import battle, team, tilemap, unit, vector

_battle = None


def get_battle():
    global _battle
    if not _battle:
        player_team = team.Team(
            units=[unit.Unit(
                image=loader.get_loader().image("hero.png"),
                position=vector.Vector2(1, 1),
                stats=None,
            )],
            controller=None,
        )

        map_1 = tilemap.TileMap(
            config.MAP_SIZE.x,
            config.MAP_SIZE.y,
            config.TILE_SIZE
        )

        _battle = battle.Battle(
            _map=map_1,
            teams=(
                player_team,
            )
        )
    return _battle


