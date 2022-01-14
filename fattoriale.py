#creare una funzione ricorsiva per calcolare il fattoriale di un numeri
def fattoriale(num,prod):
    if num > 1:
        prod = num*prod
        return fattoriale(num-1,prod)
    else:
        return prod

num = int(input("inserisci un numero: "))
prod = 1
print(f"{num}! = {fattoriale(num,prod)}")
    