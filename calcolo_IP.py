def bin2dec(binario):
    convertito = 0
    
    for k in range(len(binario)):
        if binario[k] == '0':
            pass
        if binario[k] == '1':
            convertito += 2 ** (len(binario) - k - 1)
    return convertito


def dec2bin(num, nbit):
    convertito = bin(num)[2:]
    convertito ='0'*(nbit-len(convertito))+convertito
    return convertito


def conversioneMask(mask):
    striga = ""
    striga = '1'*mask
    rimaneti = 32-mask
    striga += '0'*rimaneti
    conversione = IP_bin2dec(striga)
    print(f"la maschera di rete {conversione}")


def IP_dec2bin(ipDec):
    conversione = ""
    ip = ipDec.split('.')

    for elemento in ip:
        conversione += dec2bin(int(elemento),8)

    return conversione


def IP_bin2dec(ipBin):
    lista = []
    convertito = ""
    lista.append(ipBin[0:8]) #separo ip  in blocchi da 8 bit
    lista.append(ipBin[8:16])
    lista.append(ipBin[16:24])
    lista.append(ipBin[24:32])

    for elemento in lista:  #converto la stringa di 8 bit in un numero decimale
        convertito += str(bin2dec(elemento))+'.'
    
    return convertito[:-1]


def controlloIP(ip_rete, mask):
    conversione = IP_dec2bin(ip_rete)
    errore = False
    k=mask+1

    while errore == False and k<len(conversione):
        if conversione[k] == '0':
            k += 1
        else:
            errore = True
    
    return errore
    

def calcoloBroadcast(ip_rete,mask):
    conversione = IP_dec2bin(ip_rete)
    appoggio = conversione[:mask]

    for _ in range(32-mask+1):
        appoggio += '1'

    return IP_bin2dec(appoggio)


def calcoloPrimo(ip_rete):
    conversione = IP_dec2bin(ip_rete)
    appoggio = conversione[:-1]+'1'

    return IP_bin2dec(appoggio)

def calcoloUltimo(ip_broad):
    conversione = IP_dec2bin(ip_broad)
    appoggio = conversione[:-1]+'0'

    return IP_bin2dec(appoggio) 


def presaMaskDecimale(mask):
    convertito = IP_dec2bin(mask)
    conta = presaMaskBinaria(convertito)

    return conta


def presaMaskBinaria(mask):
    conta = 0

    for k in mask:
        if k == '1':
            conta += 1
    
    return conta


def calcoloNHost(mask):
    return 2**(32-mask)-2


def main():
    IP_rete = input("inserisci l'IP della rete: ")
    sub_mask = (input("inserisci la Subnet mask: "))

    if sub_mask[0] == '/':
        sub_mask = int(sub_mask[1:])

    elif len(sub_mask)<3:
        sub_mask = int(sub_mask)

    elif len(sub_mask)<16:
        sub_mask = presaMaskDecimale(sub_mask)

    elif len(sub_mask)<33:
        sub_mask = presaMaskBinaria(sub_mask)

    else:
        print("SUBNET MASK ERRATA")
        exit()

    errore = controlloIP(IP_rete,sub_mask)
    if errore == True:
        while(errore == True):
            print("ERRORE")
            IP_rete = input("inserisci l'IP della rete: ")
            errore = controlloIP(IP_rete,sub_mask)
            

    conversioneMask(sub_mask)

    ipBrod = calcoloBroadcast(IP_rete,sub_mask)
    ipPrimo = calcoloPrimo(IP_rete)
    ipUltimo = calcoloUltimo(ipBrod)


    print(f"il primo IP: {ipPrimo}")
    print(f"l' ultimo IP: {ipUltimo}")
    print(f"IP di Broadcast: {ipBrod}")

    print(f"il numero di host disponibili è {calcoloNHost(sub_mask)}")


if __name__ == "__main__":
    main()