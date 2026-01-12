import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def riempi_dd_anno(self):
        for year in self._model.years:
            self._view.dd_anno.options.append(ft.DropdownOption(key = year, text = year))
        self._view.update()

    def handle_dd_anno(self, e):
        self._view.txt_out_squadre.controls.clear()
        year = int(self._view.dd_anno.value)
        self._model.get_teams(year)
        num_squadre = len(self._model.teams)
        self._view.txt_out_squadre.controls.append(ft.Text(f"Numero squadre: {num_squadre}"))
        for team in self._model.teams:
            self._view.txt_out_squadre.controls.append(ft.Text(f"{team.code} ({team.name})"))
            self._view.dd_squadra.options.append(ft.DropdownOption(key = team,
                                                                text = f"{team.code} ({team.name})"))
        self._view.pulsante_crea_grafo.disabled = False
        self._view.update()


    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        self._model.crea_grafo()
        self._view.pulsante_dettagli.disabled = False
        self._view.pulsante_percorso.disabled = False
        self._view.update()

    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        self._view.txt_risultato.controls.clear()
        team = self._view.dd_squadra.value
        lista_dettagli = self._model.get_dettagli(team)
        print(team)
        print(lista_dettagli)
        for riga in lista_dettagli:
            self._view.txt_risultato.controls.append(ft.Text(str(riga)))
        self._view.update()



    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        percorso, peso = self._model.get_percorso()
        self._view.txt_risultato.controls.clear()
        for i in range(len(percorso)-1):
            nodo_1 = percorso[i]
            nodo_2 = percorso[i+1]
            peso_arco = self._model.G[nodo_1][nodo_2]["weight"]
            riga = f"{nodo_1} -> {nodo_2} ({peso_arco})"
            self._view.txt_risultato.controls.append(ft.Text(riga))
        self._view.txt_risultato.controls.append(ft.Text(f"Peso totale: {peso}"))
        self._view.update()


    """ Altri possibili metodi per gestire di dd_anno """""
    # TODO