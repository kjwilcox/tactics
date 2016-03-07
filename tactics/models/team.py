class Team:
    def __init__(self, units, controller):
        self.units = units
        self.controller = controller

    def draw(self):
        for unit in self.units:
            unit.draw()
