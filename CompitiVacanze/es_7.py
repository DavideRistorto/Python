#es 7
def scegliData():       #scelta data della spesa
    mese = input("mese del acquisto della spesa: ")
    anno = input("anno del acquisto della spesa: ")
    return mese[0].upper()+mese[1:],anno

def scelta():   #scelta elementi della spesa
    lista = []
    for _ in range (5):
        articolo =  str(input("inseririsci un articolo: "))
        lista.append(articolo)
    return lista

def caricaDati(righe):
    matrice = []
    for linea in righe: 
        stringa = linea.split(';')
        matrice.append(stringa)
    return matrice

f = open("./prezzi.csv","r")
righe = f.readlines()
matrice = caricaDati(righe)
indiceRighe,indiceCol = 0,0

mese,anno =scegliData()
articoli =scelta()         #["Birra nazionale (cl. 100)","Acqua minerale (cl. 900)"]       
prezzoSpesa,prezzoMax,prezzoMin = 0,0,10000
annoMax,meseMax = "",""
annoMin,meseMin = "",""
indiciProdotto = [] #usato per memorizzare la colonna del vari prodotti

for elemento in articoli:  #calcolatore della spesa sapendo la data
    for k in range(len(matrice)):
        for j in range(len(matrice[k])):
            if matrice[k][j] == elemento:  # si trova la colonna dell'ariticolo
                indiceCol = j                
            if matrice[k][0] == anno and matrice[k][1] == mese: #si trova la riga in base alla data
                indiceRighe = k
    prezzoSpesa += float(matrice[indiceRighe][indiceCol])  #usando la matrice e gli indici si ottiene il prezzo
    indiciProdotto.append(indiceCol) 

for k in range(1,len(matrice)):  #calcolatore del prezzo max e min dati i prodotti
    prezzo = 0                   #ciclando si cambia anno e mese
    for indice in indiciProdotto:   #si ottiene il prezzo della spesa degli articoli
        prezzo += float(matrice[k][indice])
    if prezzo > prezzoMax:
        prezzoMax = prezzo
        annoMax = matrice[k][0]
        meseMax = matrice[k][1]
    if prezzo < prezzoMin:
        annoMin = matrice[k][0]
        meseMin = matrice[k][1]
        prezzoMin = prezzo

print(f"costo della spesa oggi { round(prezzoSpesa,2)}")
print(f"spesa col costo maggiore: {meseMax}  {annoMax} -> {round(prezzoMax,2)}€")
print(f"spesa col costo minore: {meseMin}  {annoMin} -> {round(prezzoMin,2)}€")
f.close()