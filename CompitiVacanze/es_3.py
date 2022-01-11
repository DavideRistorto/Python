#mettere in ordine casuale gli elemeti di una lista
import random

lista = [1,2,3,4,5,6,"ciao"]
appoggio = []

for _ in range(len(lista)):
    scelta = random.choice(lista)
    appoggio.append(scelta)
    lista.remove(scelta)
lista = appoggio
print(lista)
