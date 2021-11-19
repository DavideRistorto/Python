tavola = [(x*y) for x in range(11) for y in range(11)]

indice1 = 0
indice2 = 11

for k in range(11):  #metodo piu lungo per dare una formattazione
    print(tavola[indice1:indice2])
    indice1+=11
    indice2+=11


    
