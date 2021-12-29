#Il file covid-19_gen1.txt contiene la sequenza genomica RNA di un virus SARS-COV-2.
#crea undizionario Python avente come chiavi i nucleotidi A, T, C, G e come
#valori i rispettivi conteggi.
f = open("./covid-19_gen1.txt","r")
lista = []
lista = f.read()
dati = {'A':0,'T':0,'C':0,'G':0}

for elemento in lista:
    if elemento in dati:
        dati[elemento] += 1
print(dati)
