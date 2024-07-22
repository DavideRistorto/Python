#stampare su file i primi 100 numeri primi
def numeroPrimo( valore):
    divisore = 2 
    primo = True  
    
    while (divisore<=valore/2) & (primo==True):  
        if valore%divisore == 0:
            primo = False
        else:
           divisore =  divisore + 1 
    return primo

f = open("./numeriPrimi.txt","w")
conta = 0
num=0
while conta<100:
    if(numeroPrimo(num)==True):
        f.write(str(num)+'\n') 
        conta+=1
    num+=1
 
f.close()
