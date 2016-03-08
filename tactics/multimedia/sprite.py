import pyglet


class Sprite:
    def __init__(self, image, coord, batch=None):
        self._pyglet_sprite = pyglet.sprite.Sprite(
            image,
            x=coord.x, y=coord.y,
            batch=batch.pyglet_batch,
        )

    def draw(self):
        self._pyglet_sprite.draw()


class SpriteBatch:
    def __init__(self):
        self.pyglet_batch = pyglet.graphics.Batch()

    def draw(self):
        self.pyglet_batch.draw()
