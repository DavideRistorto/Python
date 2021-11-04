#inserire due numeri (cordinate) in una tupla e calcolare la distanza 

x = int(input("inserisci il valore x: "))   #input delle cordinate
y = int(input("inserisci il valore y: "))
punto1 = (x,y)   #messe in una tubla
print(punto1)

x1 = int(input("inserisci il valore x: "))
y1 = int(input("inserisci il valore y: "))
punto2 = (x1,y1)
print(punto2)


if  punto1[0]>punto2[0]:         #controllo per trovare i due cateti del triangolo
    distanza_x = punto1[0]-punto2[0]
else:
    distanza_x = punto2[0]-punto1[0]

if  punto1[1]>punto2[1]:
    distanza_y = punto1[1]-punto2[1]
else:
    distanza_y = punto2[1]-punto1[1]
print(distanza_x,distanza_y)

distanza_tot = (distanza_y**2+distanza_x**2)**(1/2)  #formula del teorema di pitagora
print(f'la distanza euclidea dei due punti è {distanza_tot}')
