
# Clase para representar a un equipo
class Mapa:
    """
    Abstraccion de un mapa de overwatch
    """
    def __init__(self, tipo, name, winrate) -> None:
        self.name = name
        self.tipo = tipo
        self.winrate = winrate
