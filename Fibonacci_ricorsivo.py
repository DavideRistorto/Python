#stampare i numeri della serie fi Fibonacci minori ad un numero dato 

def fibonacci(num,a,b):
    if num > a:
        print(a)
        a,b = b,a+b
        return fibonacci(num,a,b)
    else:
        pass

num=int(input('inserisci un numero: '))
a,b = 1,1
fibonacci(num,a,b)
