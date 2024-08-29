#es 3: se nome e password sono giusti ti chiedo vuoi modificare il tuo profilo? altrimenti creo un profilo fittizio
nome=input('nome utente: ')
password=input('password: ')

nome_utente_corretto = "utente123"
password_corretta = "password123"

if nome==nome_utente_corretto and password==password_corretta:
    x=input('Benvenuto, vuoi modificare il tuo profilo? Rispondi sì o no: ')
    if x=='sì':
        nome=input('nuovo nome utente: ')
        password=input('nuova password: ')
    elif x=='no':
        print('hai scelto di non modificare il tuo profilo')
    else:
        print('errore')
else:
    print('creazione profilo')
    nome_profilo=nome
    password_profilo=password