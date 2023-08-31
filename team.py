
# Clase para representar a un equipo
class Team:
    """
    Clase para modelar a un equipo de valorant
    """
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def is_team_alive(self):
        return any(player.is_alive() for player in self.players)