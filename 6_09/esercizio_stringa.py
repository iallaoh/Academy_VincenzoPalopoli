
#decoratore controlla lunghezza stringa
def verifica_compressione(funzione_compressione):
    def wrapper(stringa):
        # esecuzione compressione
        stringa_compressa = funzione_compressione(stringa)
        
        # controllo se la stringa compressa è più lunga della stringa originale
        if len(stringa_compressa) >= len(stringa):
            return stringa
        return stringa_compressa
    return wrapper

#funzione che comprime la stringa
@verifica_compressione
def compressione(stringa):
    stringa_compressa = []
    conteggio = 1

    for i in range(1, len(stringa)):
        if stringa[i] == stringa[i-1]:
            conteggio += 1
        else:
            stringa_compressa.append(f"{stringa[i-1]}{conteggio}")
            conteggio = 1

    stringa_compressa.append(f"{stringa[-1]}{conteggio}")
    
    return ''.join(stringa_compressa)

# inserimento stringa
stringa = input("inserisci stringa: ")
stringa_compressa = compressione(stringa)

print("Stringa risultante:", stringa_compressa)


