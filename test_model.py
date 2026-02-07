from model.model import Model

model = Model()

model.get_team(1985)
model.handle_grafo()
a = model.handle_dettagli(1942)
print(a)

b, c = model.ricerca_percorso(1942)

print(b)
print(c)