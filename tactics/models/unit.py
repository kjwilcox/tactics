import pyglet

from tactics import config


class Unit:
    def __init__(self, image, position, stats):
        self.image = image
        self.position = position
        self.stats = stats

        self._sprite = pyglet.sprite.Sprite(
            self.image,
            x=position.x*config.TILE_SIZE,
            y=position.y*config.TILE_SIZE,
            subpixel=True,
        )

    def draw(self):
        self._sprite.draw()
