#es1 

username_corretto = "admin"
password_corretta = "12345"

# Richiesta di input dall'utente
username = input("Inserisci il tuo nome utente: ")
password = input("Inserisci la tua password: ")

# Verifica delle credenziali
if username == username_corretto and password == password_corretta:
    print("Benvenuto, sei loggato con successo!")
    
    # Modifica dei dati dopo il login
    print("Puoi rispondere a una domanda segreta.")
    scelta = input("Scegli 1 per il colore preferito o 2 per l'animale preferito: ")
    
    if scelta == "1":
        colore_preferito = input("Qual è il tuo colore preferito? ")
        print(f"Il tuo colore preferito è {colore_preferito}.")
    elif scelta == "2":
        animale_preferito = input("Qual è il tuo animale preferito? ")
        print(f"Il tuo animale preferito è {animale_preferito}.")
    else:
        print("Scelta non valida.")
else:
    print("Nome utente o password errati. Riprova.")