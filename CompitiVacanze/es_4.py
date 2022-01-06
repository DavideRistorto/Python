#FORZA 4 da terminale
import os
import numpy as np #implementare gli array
campo = np.array([[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]) #campo/matrice 6*7
indici = '  1 -  2 - 3 - 4 - 5 - 6 - 7'

def partita(campo,g1,g2):   
    contaMosse = 42  #usato per situazione di pareggio da campo pieno
    vittoria = False
    print(indici)
    print(campo)
    while contaMosse>0 and vittoria == False:   #presa input della mossa 
        if contaMosse%2==0: #si alternano i due giocatori
            posizione = int(input(f"\n{g1} scegli la colonna della posizione (1-7):  "))
            posizione = cotrolloInput(posizione)
            carattere = 'O'
        if contaMosse%2!=0:
            posizione = int(input(f"\n{g2} scegli la colonna della posizione (1-7):  "))
            posizione = cotrolloInput(posizione)
            carattere = 'X'
        posizione -=1
        messa = False
        contaRighe = 5
        while messa == False and contaRighe>=0: #ciclo che continua finche la mossa non viene messa in campo
            if campo[contaRighe][posizione]==' ':
                os.system('clear')
                campo[contaRighe][posizione] = carattere
                messa = True
            else:
                contaRighe -=1
                if(contaRighe == 0):    #controllo se la colonna è piena
                    os.system('clear')
                    print("COLONNA PIENA! RINSERISCI\n")
                    contaMosse += 1   # la mossa viene annullata
                    
        print(f'\n{indici}')
        print(campo)
        
        vittoria = controlloVittoria()
        if vittoria == True and carattere == 'O':
            print(f"{g1} HA VINTO LA PARTITA")
        elif vittoria == True and carattere == 'X':
            print(f"{g2} HA VINTO LA PARTITA")
        contaMosse -=1
    if(contaMosse==0):
        print("PAREGGIO: TAVOLA PIENA")

def cotrolloInput(posizione):   #controllo input mossa
    while posizione<1 or posizione >7:
        posizione = int(input("rinserisci la posizione della mossa:"))
    return posizione

def controlloVittoria():
    indiceRiga,indiceCol = 5,0
    vittoria = False
    while vittoria == False and indiceRiga>0 : #controllo orizzontale su tutte le righe 
        if campo[indiceRiga][indiceCol]==campo[indiceRiga][indiceCol+1]==campo[indiceRiga][indiceCol+2]==campo[indiceRiga][indiceCol+3] and campo[indiceRiga][indiceCol]!=' ':
            vittoria = True
        else:
            indiceCol += 1
        if indiceCol == 4:
            indiceCol = 0
            indiceRiga -= 1

    indiceRiga,indiceCol = 5,0
    while vittoria == False and indiceCol < 7: #controllo verticale su tutte le colonne
        if campo[indiceRiga][indiceCol]==campo[indiceRiga-1][indiceCol]==campo[indiceRiga-2][indiceCol]==campo[indiceRiga-3][indiceCol] and campo[indiceRiga][indiceCol]!=' ':
            vittoria = True
        else:
            indiceRiga -= 1
        if indiceRiga == 2:
            indiceCol += 1
            indiceRiga = 5

    indiceRiga,indiceCol = 5,0
    while vittoria == False and indiceCol < 4: #controllo obliquo DX /
        if campo[indiceRiga][indiceCol]==campo[indiceRiga-1][indiceCol+1]==campo[indiceRiga-2][indiceCol+2]==campo[indiceRiga-3][indiceCol+3] and campo[indiceRiga][indiceCol]!=' ':
            vittoria = True
        else:
            indiceRiga -= 1
        if indiceRiga == 2:
            indiceCol += 1
            indiceRiga = 5

    indiceRiga,indiceCol = 5,6
    while vittoria == False and indiceCol > 2: #controllo obliquo SX \
        if campo[indiceRiga][indiceCol]==campo[indiceRiga-1][indiceCol-1]==campo[indiceRiga-2][indiceCol-2]==campo[indiceRiga-3][indiceCol-3] and campo[indiceRiga][indiceCol]!=' ':
            vittoria = True
        else:
            indiceRiga -= 1
        if indiceRiga == 2:
            indiceCol -= 1
            indiceRiga = 5

    return vittoria

g1 = input("inserisci nome giocatore 1: ")
g2 = input("inserisci nome giocatore 2: ")

partita(campo,g1,g2)