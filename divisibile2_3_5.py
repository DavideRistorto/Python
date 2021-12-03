def divisibile(num):
    if num %2 == 0:
        print("il numero inserito è divisibile per 2")
    if num % 3 == 0:
         print("il numero inserito è divisibile per 3")
    if num %5 == 0:
         print("il numero inserito è divisibile per 5")

num = int(input("metti numero: "))
divisibile(num)