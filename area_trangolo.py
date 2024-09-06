#area triangolo
def area_triangolo(base, altezza):
    return base*altezza/2
    
#area quadrato
def area_quadrato(lato):
    return lato**2

#area rettangolo
def area_rettangolo(base, altezza):
    return base*altezza

#lista
lista_risultati_triangolo=[]
lista_risultati_quadrato=[]
lista_risultati_rettangolo=[]


while True:
    scelta=int(input("qual è la figura di cui vuoi calcolare l'area? 1: triangolo, 2: quadrato, 3: rettangolo"))
    if scelta==1:
        base=int(input("qual è la base? "))
        altezza=int(input("qual è l'altezza? "))
        risultato=area_triangolo(base, altezza)
        lista_risultati_triangolo.append(risultato)
    elif scelta==2:
        lato=int(input("qual è la base? "))
        risultato=area_quadrato(lato)
        lista_risultati_quadrato.append(risultato)
    elif scelta==3:
        base=int(input("qual è la base? "))
        altezza=int(input("qual è l'altezza? "))
        risultato=area_rettangolo(base, altezza)
        lista_risultati_rettangolo.append(risultato)
    else:
        print("errore")
        continue
    
        

