import random

import pyrsistent

from tactics.models import tile, vector
from tactics import multimedia


class TileMap:
    def __init__(self, x_size, y_size, tile_size):
        self.size = pyrsistent.m(x=x_size, y=y_size)

        tile_types = [
            tile.GrassTile,
            tile.GrassTile,
            tile.WaterTile,
        ]

        self.tiles = {
            vector.Vector2(x, y): random.choice(tile_types)()
            for x in range(x_size)
            for y in range(y_size)
        }

        self.sprite_batch = multimedia.SpriteBatch()

        self.sprites = pyrsistent.pmap({
            coord: multimedia.Sprite(
                self.tiles[coord].image,
                vector.Vector2(
                    x=coord.x*tile_size,
                    y=coord.y*tile_size,
                ),
                batch=self.sprite_batch,
            )
            for coord in self.tiles
        })

    def draw(self):
        self.sprite_batch.draw()

