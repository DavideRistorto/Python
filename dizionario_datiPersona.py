#chiedere i dati dell utente, salvarli in un dizionario e scriverli su file
f = open("./datiDizionario.txt","w")
nome = input("inserisci il tuo nome: ")
cognome = input("inserisci il tuo cognome: ")
nascita = input("inserisci la tua data di nascita: ")

dati = {"persona":{"cognome":cognome, "nome":nome, "nascita":nascita }}
print(dati["persona"])
f.write(str(dati["persona"]))
f.close()

