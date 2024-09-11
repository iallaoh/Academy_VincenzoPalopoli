#es libro, creare classe libro con attributi autore titolo e pagine, metodo descrizione che stampa il libro titolo è stato scritto da autore e ha pagine pagine

class Libro:
    def __init__(self, titolo, autore, pagine):
        # Ciclo per assicurarsi che titolo e autore non siano vuoti
        while titolo == "" or autore == "":
            print("Titolo e autore non possono essere vuoti.")
            titolo = input("Inserisci il titolo: ")
            autore = input("Inserisci l'autore: ")
        
        # Ciclo per assicurarsi che il numero di pagine sia positivo
        while pagine <= 0:
            print("Il numero di pagine deve essere positivo.")
            pagine = int(input("Inserisci il numero di pagine: "))
        
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        print(f"Il libro '{self.titolo}' è stato scritto da {self.autore} e ha {self.pagine} pagine.")
        
titolo = input("Inserisci il titolo: ")
autore = input("Inserisci l'autore: ")
pagine = int(input("Inserisci il numero di pagine: "))

mio_libro = Libro(titolo, autore, pagine)
mio_libro.descrizione()