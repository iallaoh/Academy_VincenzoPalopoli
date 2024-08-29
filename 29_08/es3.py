#es3

#inserimento input

primo_numero=int(input('inserisci il primo numero: '))
secondo_numero=int(input('inserisci il secondo numero: '))
print('le operazioni algebriche possibili sono: ')
print('1: addizione')
print('2: sottrazione')
print('3: moltiplicazione')
print('4: divisione')
operazione=int(input("inserisci il numero dell'operazione che vuoi effettuare: "))

#controllo condizioni
if operazione==1:
    addizione=primo_numero+secondo_numero
    print(f"il risultato è {addizione}")
elif operazione==2:
    sottrazione=primo_numero-secondo_numero
    print(f"il risultato è {sottrazione}")
elif operazione==3:
    moltiplicazione=primo_numero*secondo_numero
    print(f"il risultato è {moltiplicazione}")
else:
    if secondo_numero==0:
        secondo_numero=int(input('il divisore non può essere 0, scegli un altro numero'))
    else:
        divisione=primo_numero/secondo_numero
        print(f"il risultato è {divisione}")


