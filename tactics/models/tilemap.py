import random

import pyglet
import pyrsistent

from tactics.models import tile, vector


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

        self.sprite_batch = pyglet.graphics.Batch()
        self.sprites = pyrsistent.pmap({
            coord: pyglet.sprite.Sprite(
                self.tiles[coord].image,
                x=coord.x*tile_size, y=coord.y*tile_size,
                batch=self.sprite_batch
            )
            for coord in self.tiles
        })

    def draw(self):
        self.sprite_batch.draw()

