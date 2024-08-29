#es 2: eseguire un'operazione su quella stringa in base a ciò che sceglie l'utente
x=input('digitare testo: ')
opzione=chr(input('a: aggiungi, b: rimuovi, c: cambia'))
if opzione=='a':
    nuova=input('parola da aggiungere: ')
    x=x+''+nuova
    print('testo aggiornato: ', x, '.')
elif opzione=='b':
    nuova=input('parola da rimuovere: ')
    x=nuova
    print('testo aggiornato: ', x, '.')
elif opzione=='c':
    x=''
    print('testo eliminato')
else:
    print('errore')