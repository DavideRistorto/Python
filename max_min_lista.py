#data una lista trovare il valore maggiore e minore al suo interno
lista = [4,53,76,3,6,1]
dimensione = len(lista)
max = lista[0]
min = lista[0]

for elemento in lista:
    if elemento > max:
        max = elemento

    elif elemento<min:
        min = elemento

print(f'il numero piu grande è {max}  mentre il numero più piccolo è {min}')

