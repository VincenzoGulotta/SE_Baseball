import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_dd_anno(self):
        lista_anni = self._model.get_anni()
        for anno in lista_anni:
            self._view.dd_anno.options.append(ft.DropdownOption(key = anno, text = anno))
        self._view.update()

    def mostra_teams(self, e):
        self._view.txt_out_squadre.controls.clear()
        self._view.dd_squadra.options.clear()
        anno = self._view.dd_anno.value
        teams = self._model.get_team(anno)
        if teams:
            self._view.txt_out_squadre.controls.append(ft.Text(f"Numero squadre: {len(teams)}"))
            for team in teams:
                self._view.txt_out_squadre.controls.append(ft.Text(team))
                self._view.dd_squadra.options.append(ft.DropdownOption(key = team.team_id, text = team))
            self._view.pulsante_crea_grafo.disabled = False
            self._view.update()
        else:
            self._view.show_alert("Non sono presenti dati inerenti l'anno selezionato")


    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        self._model.handle_grafo()
        self._view.dd_squadra.disabled = False
        self._view.update()


    def abilita_pulsanti(self, e):
        self._view.pulsante_dettagli.disabled = False
        self._view.pulsante_percorso.disabled = False
        self._view.update()

    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        self._view.txt_risultato.controls.clear()
        team_id = int(self._view.dd_squadra.value)
        dict_stipendi = self._model.handle_dettagli(team_id)
        for team_salary in dict_stipendi:
            stipendio = team_salary[1]
            team = team_salary[0]
            self._view.txt_risultato.controls.append(ft.Text(f"{team} - peso {stipendio}"))

        self._view.update()

    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        self._view.txt_risultato.controls.clear()
        team_id = int(self._view.dd_squadra.value)
        lista_archi, peso_max = self._model.ricerca_percorso(team_id)
        for arco in lista_archi:
            self._view.txt_risultato.controls.append(ft.Text(f"{arco[0]} -> {arco[1]} (peso {arco[2]})"))
        self._view.txt_risultato.controls.append(ft.Text(f"Peso totale: {peso_max}"))
        self._view.update()


    """ Altri possibili metodi per gestire di dd_anno """""
    # TODO