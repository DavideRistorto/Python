#eliminare i doppioni da una lista
lista = [2, 1, 2, 3, 0, 6, 7, 6, 4, 8,"ss","ss"]
appoggio =  []
[appoggio.append(elemento) for elemento in lista if elemento not in appoggio]
#append di un elemento se non è gia presente nella lista di appoggio
lista = appoggio
print (lista)

