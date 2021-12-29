#data una lista qualsiasi la trasformi in un
#dizionario avente come chiavi gli indici della lista e come valori gli elementi
lista = ["a","b","c","d","e","f","g"]
dizionario = {x: lista[x] for x in range(len(lista))}  #dict comprehension
print(dizionario)
