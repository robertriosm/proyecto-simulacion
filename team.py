
# Clase para representar a un equipo
class Team:
    """
    Abstraccion para modelar a un equipo de overwatch
    """
    def __init__(self, name, mapa, winrate):
        self.name = name
        self.mapa = mapa
        self.winrate = winrate

    def add_player(self, player):
        self.players.append(player)

    def is_team_alive(self):
        return any(player.is_alive() for player in self.players)