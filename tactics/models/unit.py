from tactics import config
from tactics import multimedia
from tactics.models import vector


class Unit:
    def __init__(self, image, position, stats):
        self.image = image
        self.position = position
        self.stats = stats

        self._sprite = multimedia.Sprite(
            image=self.image,
            coord=vector.Vector2(
                x=position.x*config.TILE_SIZE,
                y=position.y*config.TILE_SIZE,
            )
        )

    def draw(self):
        self._sprite.draw()
