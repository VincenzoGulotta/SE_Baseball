import networkx as nx
from database.dao import DAO

class Model:

    def __init__(self):
        self.G = nx.Graph()
        self.years = DAO.get_years()
        self.teams = None
        self.squadra = None
        self.percorso = None
        self.peso = 0

    def get_teams(self, year):
        self.teams = DAO.get_squadre_anno(year)

    def crea_grafo(self):
        for team1 in self.teams:
            for team2 in self.teams:
                salary_1 = team1.salary
                salary_2 = team2.salary
                self.G.add_edge(team1, team2, weight = (salary_1 + salary_2))

    def get_dettagli(self, node):
        lista_dettagli = []

        for item in self.teams:     # Ho ricevuto come nodo una stringa, quindi la cambio in oggetto cercandolo
                                    # nella lista
            if node == f"{item.code} ({item.name})":
                self.squadra = item

        for edge in self.G.edges(self.squadra, data=True):
            nodo_2 = edge[1]
            peso = edge[2]["weight"]
            riga = f"{nodo_2} - peso {peso}"
            lista_dettagli.append(riga)

        return lista_dettagli

    def get_percorso(self):
        percorso = []
        percorso.append(self.squadra)
        self.ricorsione(self.squadra, percorso, 0)

        return self.percorso, self.peso


    def ricorsione(self, node, percorso_parz, peso_parz):
        if peso_parz > self.peso:
            self.peso = peso_parz
            self.percorso = list(percorso_parz)

        visitati = 0
        for team in self.G.neighbors(node):
            if visitati == 3:
                break
            if team not in percorso_parz:
                if len(percorso_parz) <= 1:
                    nuovo_percorso = list(percorso_parz)
                    nuovo_percorso.append(team)
                    peso = self.G[node][team]["weight"]
                    self.ricorsione(team, nuovo_percorso, peso_parz + peso)
                    visitati += 1
                else:
                    nodo_passato = percorso_parz[-2]
                    peso_passato = self.G[nodo_passato][node]["weight"]
                    peso = self.G[node][team]["weight"]
                    if peso < peso_passato:
                        nuovo_percorso = list(percorso_parz)
                        nuovo_percorso.append(team)
                        self.ricorsione(team, nuovo_percorso, peso_parz + peso)
                        visitati += 1