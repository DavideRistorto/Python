#in base alla risposta caricare una lista con numeri interi finche l'utente desidera
lista = []
risposta = 'si'
num = 0

while risposta == 'si':
   num= int(input("inserisci numero: "))
   lista.append(num)
   risposta =  str(input("se vuoi inserire un altro numero digita si : "))

print(lista)
    


