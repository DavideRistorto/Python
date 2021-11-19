#usare una lambda function per verificare se una stringa è palindroma
isPalindroma = lambda string: (string==string[::-1])    #True se la stringa è uguale a se stessa ma invertita usando [::-1]

stringa = "malayalam"
if(isPalindroma(stringa)):
    print(f"la stringa {stringa} è palindroma")
else:
     print(f"la stringa {stringa} non è palindroma")