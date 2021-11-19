#usare una lambda function per vedere se una stringa inizia con una lettera maiuscola
isMaiuscolo = lambda string: (string[0].isupper())

stringa1 = "minuscolo"
if(isMaiuscolo(stringa1)):
    print(f"la stringa: {stringa1} inizia con una lettera maiuscola")
else:
     print(f"la stringa: {stringa1} non inizia con una lettera maiuscola")

     


