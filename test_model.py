from model.model import Model

model = Model()

for item in model.years:
    print(item)

model.get_teams(2015)

for teams in model.teams:
    print(teams)

model.crea_grafo()
righe = model.get_dettagli("ATL (Atlanta Braves)")

for riga in righe:
    print(riga)