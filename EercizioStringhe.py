word = "parolina"
 #stampa prima e ultima lettera
print(f"la prima lettera è: {word[0]} l'ultima lettera è: {word[-1]} ") 

#stampa la parola senza la lettera inziale e finale
print(word[1:-1])

#stampa una lettera si e una no
print(word[:-1:2])

#stampare parola invertita
print(word[::-1])

#stampare '?' come terzo carattere della stringa
newWord = word[0:2] + '?' + word[3:]
print(newWord)



