#data una lista di stringhe ricavare una lista con le stringhe palindrome
# e un'altra con le stringhe che iniziano con una maiuscola

listaString = ["ciao","Ciao","anna","AnnA","malayalam","Buonasera"]
listaPalindrome = []
listaMaiuscole = []

for elemento in listaString:
    if elemento == elemento[::-1]:
        listaPalindrome.append  (elemento)

    if elemento[0].isupper():
        listaMaiuscole.append (elemento)

print(f"stringhe palindrome: {listaPalindrome}")
print(f"stringhe con lettera maiuscola iniziale: {listaMaiuscole}")
