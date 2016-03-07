from tactics import loader


class Tile:
    def draw(self):
        pass


class GrassTile(Tile):
    name = "Grass"
    image = loader.get_loader().image("grass.png")
    cost = 1
    defense = 0


class WaterTile(Tile):
    name = "Water"
    image = loader.get_loader().image("water.png")
    cost = 3
    defense = 0
