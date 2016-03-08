from tactics import loader


class Tile:
    def __init__(self):
        self.image = loader.load_image(self.image_path)

    def draw(self):
        pass


class GrassTile(Tile):
    name = "Grass"
    image_path = "grass.png"
    cost = 1
    defense = 0


class WaterTile(Tile):
    name = "Water"
    image_path = "water.png"
    cost = 3
    defense = 0
