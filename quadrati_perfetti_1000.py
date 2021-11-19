#trovare i quadrati perfetti dispari dei numeri minori di 1000
lista = []
for k in range(1000):
    if (k**(1/2))%1 == 0 and (k**(1/2))%2 != 0:
        lista.append(k)

print(lista)
