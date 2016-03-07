import pyglet


class Sprite:
    def __init__(self, image, coord, batch=None):
        self._pyglet_sprite = pyglet.sprite.Sprite(
            image,
            x=coord.x, y=coord.y,
            batch=batch,
        )

    def draw(self):
        self._pyglet_sprite.draw()


class SpriteBatch(pyglet.graphics.Batch):
    pass