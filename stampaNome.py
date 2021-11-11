#inserire un nome da tastiera, stampare il primo carattere del nome i restanti sostituirli con *
nome = str(input('inserisci il tuo nome: '))
num = len(nome)
print(nome[0]+(num-1)*"*")
