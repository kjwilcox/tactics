class Battle:
    def __init__(self, _map, teams):
        self.map = _map
        self.teams = teams

    def draw(self):
        self.map.draw()

        for team in self.teams:
            team.draw()
