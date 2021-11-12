#creare una funzione che stabilisca se un numero è primo 
def numeroPrimo( valore):
    divisore = 2
    primo = True  
    
    while (divisore<=valore/2) & (primo==True):
        if valore%divisore == 0:
            primo = False
        else:
           divisore =  divisore + 1 
    
    return primo


num = int(input("inserisci un numero: "))

primo_ = numeroPrimo(num)

if primo_ == True:
    print(f"il numero {num} è primo")
else:
        print(f"il numero {num} non è primo")

    
