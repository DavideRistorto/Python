# stabilire il numero di numeri primi minori di 1000
def numeroPrimo( valore):
    divisore = 2
    primo = True  
    
    while (divisore<=valore/2) & (primo==True):
        if valore%divisore == 0:
            primo = False
        else:
           divisore =  divisore + 1 
    
    return primo

conta=0

for num in range(1,1000):
    if numeroPrimo(num):
        conta+=1
print(f"i numeri primi minori di 1000 sono {conta}")
