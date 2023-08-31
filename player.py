
class Player:
    """
    Clase para representar a un jugador con nivel de habilidad
    """
    def __init__(self, name, health, shield, weapon_damage, special_ability, skill_level):
        self.name = name
        self.health = health
        self.shield = shield
        self.weapon_damage = weapon_damage
        self.special_ability = special_ability
        self.skill_level = skill_level



    def is_alive(self):
        """
        Función para determinar si un jugador sigue con vida
        """
        return self.health > 0
    


    def attack(self, opponent):
        """
        Función para simular que un jugador ataca a otro
        """
        effective_damage = self.weapon_damage * self.skill_level
        if opponent.shield > 0:
            opponent.shield -= effective_damage
            if opponent.shield < 0:
                opponent.health += opponent.shield
                opponent.shield = 0
        else:
            opponent.health -= effective_damage

    def use_special_ability(self):
        """
        Función para simular el uso de una habilidad especial
        """
        self.weapon_damage *= (self.special_ability * self.skill_level)