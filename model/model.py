from math import inf

import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.dict_team = None
        self.percorso = None
        self.peso = 0

    def get_anni(self):
        lista_anni = DAO.get_anni()
        return lista_anni

    def get_team(self, anno):
        self.dict_team = DAO.get_squadre_stipendi(anno)
        teams = []
        for team_id in self.dict_team.keys():
            team = self.dict_team[team_id]
            teams.append(team)

        return teams

    def handle_grafo(self):
        for team_id_1 in self.dict_team.keys():
            team1 = self.dict_team[team_id_1]
            peso1 = team1.salary
            self.G.add_node(team1)
            for team_id_2 in self.dict_team.keys():
                if team_id_1 != team_id_2:
                    team2 = self.dict_team[team_id_2]
                    peso2 = team2.salary
                    self.G.add_edge(team1, team2, weight = peso1 + peso2)

    def handle_dettagli(self, team_id):
        team1 = self.dict_team[team_id]
        dict_stipendi = {}
        for team2 in self.G.neighbors(team1):
            peso = self.G[team1][team2]['weight']
            team_tag = f"[{team2.code}] ({team2.name})"
            dict_stipendi[team_tag] = peso

        sorted_dict = sorted(dict_stipendi.items(), key = lambda x: x[1], reverse = True)
        return sorted_dict


    def ricerca_percorso(self, team_id):
        self.percorso = None
        self.peso = 0
        team = self.dict_team[team_id]
        peso = float(inf)
        self.ricorsione([team], 0, team, peso)

        lista_archi = []
        if self.percorso:
            for i in range(len(self.percorso)-1):
                team1 = self.percorso[i]
                team2 = self.percorso[i+1]
                peso = self.G[team1][team2]['weight']
                arco = [team1, team2, peso]
                lista_archi.append(arco)

        return lista_archi, self.peso

    def ricorsione(self, percorso_parziale, peso_parziale, vecchio_team, vecchio_peso):
        if peso_parziale > self.peso:
            self.peso = peso_parziale
            self.percorso = percorso_parziale

        i = 0
        for nuovo_team in self.G.neighbors(vecchio_team):
            if i < 3:
                if nuovo_team not in percorso_parziale:
                    nuovo_peso = self.G[vecchio_team][nuovo_team]['weight']
                    if nuovo_peso < vecchio_peso:
                        nuovo_percorso = list(percorso_parziale)
                        nuovo_percorso.append(nuovo_team)
                        i += 1
                        self.ricorsione(nuovo_percorso, peso_parziale + nuovo_peso, nuovo_team, nuovo_peso)
            else:
                break