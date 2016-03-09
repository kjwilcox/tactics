import functools

from tactics import config
from tactics.models import battle, team, tilemap, unit, vector
from tactics.multimedia import loader


@functools.lru_cache()
def get_battle():

    player_team = team.Team(
        units=[
            unit.Unit(
                image=loader.load_image("hero.png"),
                position=vector.Vector2(1, 1),
                stats=None,
            ),
            unit.Unit(
                image=loader.load_image("hero.png"),
                position=vector.Vector2(7, 3),
                stats=None,
            ),
        ],
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


