#prendere due num in input, fare delle espressioni e i risultati metterli in una lista

x = int(input("metti un numero: "))
y = int(input("metti un numero: "))
lista = []  #inizializzo lista vuota
quandrato1 = (x**x)+(y**y)
lista.append(quandrato1)

quandrato2 =(x+y)**2
lista.append(quandrato2)

quadrato3 = (x**x)-(y**y)
lista.append(quadrato3)

quandrato4 = quadrato3
lista.append(quandrato4)

print(lista)










