#area triangolo
def area_triangolo(base, altezza):
    base=int(input("qual è la base? "))
    altezza=int(input("qual è l'altezza? "))
    return base*altezza/2
    
#area quadrato
def area_quadrato(lato):
    return lato**2

#area rettangolo
def area_rettangolo(base, altezza):
    return base*altezza

#liste
lista_risultati_triangolo=[]
lista_risultati_quadrato=[]
lista_risultati_rettangolo=[]

#
def calcolo_area(scelta):
    if scelta==1:
        base=int(input("qual è la base? "))
        altezza=int(input("qual è l'altezza? "))
        risultato=area_triangolo(base, altezza)
        print(f"il risultato è {risultato}")
        lista_risultati_triangolo.append(risultato)
    elif scelta==2:
        lato=int(input("qual è la base? "))
        risultato=area_quadrato(lato)
        print(f"il risultato è {risultato}")
        lista_risultati_quadrato.append(risultato)
    elif scelta==3:
        base=int(input("qual è la base? "))
        altezza=int(input("qual è l'altezza? "))
        risultato=area_rettangolo(base, altezza)
        print(f"il risultato è {risultato}")
        lista_risultati_rettangolo.append(risultato)
    elif scelta==0:
        print("Uscita dal programma.")
    else:
        print("errore")


#decoratore
def decoratore_calcolo_area(iterazione):
    def wrapper():
        while True:
            scelta=int(input("qual è la figura di cui vuoi calcolare l'area? 1: triangolo, 2: quadrato, 3: rettangolo, 0: esci"))
            if scelta==0:
                print("Grazie per aver usato il calcolatore di aree!")
                break
            calcolo_area(scelta)
    return wrapper

@decoratore_calcolo_area
def calcolo_area_decorata(scelta):
    calcolo_area(scelta)

#eseguo la funzione        
calcolo_area_decorata()


