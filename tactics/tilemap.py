import random

import pyglet
import pyrsistent




class TileMap:
    def __init__(self, x_size, y_size, tile_size):
        self.size = pyrsistent.m(x=x_size, y=y_size)
        grass_image = pyglet.resource.image("grass.png")
        water_image = pyglet.resource.image("water.png")
        images = [grass_image, water_image]

        self.sprite_batch = pyglet.graphics.Batch()

        self.tiles = pyrsistent.pmap({
            (x, y): pyglet.sprite.Sprite(
                random.choice(images),
                x=x*tile_size, y=y*tile_size,
                batch=self.sprite_batch
            )
            for x in range(x_size)
            for y in range(y_size)
        })

    def draw(self):
        self.sprite_batch.draw()

