#creare lista compreension con potenze di due inferiori ad un limite
limite = int(input("inserisci un valore: "))
n=1
num=0
lista = [2**n for n in range(10) if(2**n)<=limite]
print(lista)  