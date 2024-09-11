from es2_classi import Libro

class Biblioteca:
    def __init__(self):
        self.libri=[]
        
    def aggiungi_libro(self):
        titolo = input("Inserisci il titolo: ")
        autore = input("Inserisci l'autore: ")
        pagine = int(input("Inserisci il numero di pagine: "))
        
        try:
            libro = Libro(titolo, autore, pagine)
            self.libri.append(libro)
            print("Libro aggiunto con successo!")
        except ValueError as e:
            print(f"Errore: {e}")
        
    def stampa_libri(self):
        if len(self.libri)==0:
            print("Non ci sono libri in biblioteca.")
        else:
            for libro in self.libri:
                print(libro.descrizione())
                
#creo la biblioteca
biblioteca=Biblioteca()

while True:
    scelta=input("Vuoi inserire un libro? si/no: ")
    if scelta=="si":
        biblioteca.aggiungi_libro()
    elif scelta=="no":
        break
    else:
        print("Scelta non valida, digita 'si' o 'no'")
        
print("Libri nella biblioteca: ", biblioteca.stampa_libri())