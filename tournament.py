import random
from mapa import Mapa
from team import Team
from collections import Counter


class Tournament:
    """
    Clase para modelar un torneo de valorant de 16-16 equipos, puede ejecutar varios
    torneos y mostrar a los equipos que mas torneos han ganado
    """

    def __init__(self) -> None:
        self.tournament_results = Counter()



    def simulate_encounter(self, team1: Team, team2: Team):
        """
        Función para simular un único encuentro entre dos equipos
        """
        while team1.is_team_alive() and team2.is_team_alive():
            for player1 in team1.players:
                if not player1.is_alive():
                    continue
                for player2 in team2.players:
                    if not player2.is_alive():
                        continue

                    if random.choice([True, False]):
                        player1.use_special_ability()
                    player1.attack(player2)

                    if random.choice([True, False]):
                        player2.use_special_ability()
                    player2.attack(player1)

        return team1 if team1.is_team_alive() else team2



    def create_random_team(self, team_name):
        """
        Función para crear un equipo con jugadores aleatorios
        """
        team = Team(team_name)
        for i in range(5):  # Cada equipo tiene 3 jugadores
            player_name = f"{team_name}_Player{i+1}"
            health = 100
            shield = 50
            weapon_damage = random.randint(15, 30)
            special_ability = random.uniform(1.1, 1.5)
            skill_level = random.uniform(0.8, 1.2)
        return team



    def simulate_tournament_round(self, teams):
        """
        Función para simular una ronda del torneo
        """
        random.shuffle(teams)  # Mezclar los equipos para emparejamientos aleatorios
        winners = []
        for i in range(0, len(teams), 2):
            team1 = teams[i]
            team2 = teams[i + 1]
            winner = self.simulate_encounter(team1, team2)
            winners.append(winner)
        return winners # 3 de 5 mapas 



    def simulate_complete_tournament(self):
        """
        Función para simular un torneo completo
        """
        # Crear 16-16 equipos
        all_teams = [self.create_random_team(f"Team{i+1}") for i in range(32)]
        
        # Iniciar el torneo
        remaining_teams = all_teams
        while len(remaining_teams) > 1:
            remaining_teams = self.simulate_tournament_round(remaining_teams)
        
        # Devolver el equipo ganador
        return remaining_teams[0].name



    def simulate_multiple_tournaments(self, n):
        """
        Función para simular multiples torneos completo
        """
        for _ in range(n):
            winner = self.simulate_complete_tournament()
            self.tournament_results[winner] += 1



    def top5_winners(self):
        """
        Función para mostrar a los primeros 5 ganadores de un torneo
        """
        try:
            return self.tournament_results.most_common(5)
        except:
            return "no se han llevado torneos a cabo!"
