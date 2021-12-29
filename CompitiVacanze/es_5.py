#Scrivere un programma in Python che prenda in input il nome file di un programma scritto in C.
#contare il numero delle righe del codice, le righe commentate e il numero di funzioni printf

f = open("./main.c","r")
righe = f.readlines()
conta = 0
contaPrintf = 0
contaCommenti,commentoUnito,commentoUnitoChiuso = 0,0,0
for linea in righe:
    conta +=1
    contaPrintf += linea.count("printf") # Il metodo count cerca e conta una determinata stringa
    contaCommenti += linea.count("//")
    commentoUnito += linea.count("/*")   #usato per verificare i commenti su più righe
    commentoUnitoChiuso += linea.count("*/")
    if(commentoUnito==1):
        contaCommenti+=1
    if commentoUnitoChiuso ==  1:
        commentoUnito = 0
        commentoUnitoChiuso = 0

print(f"righe di codice: {conta}")
print(f"funzioni printf: { contaPrintf}")
print(f"conta righe commentate: {contaCommenti}")