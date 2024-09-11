#esercizio 1: distanza dall'origine
import math

class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy
    def distanza_da_origine(self):
        return math.sqrt(self.x**2 + self.y**2)


#chiedo all'utente le coordinate
x = float(input("Inserisci la coordinata x: "))
y = float(input("Inserisci la coordinata y: "))

#inserisco le coordinate nell'oggetto punto
punto = Punto(x, y)    
print("Coordinate iniziali:", punto.x, punto.y)

#sposto il punto chiedendo le coordinate
dx = float(input("Di quanto vuoi spostare la coordinata x: "))
dy = float(input("Di quanto vuoi spostare la coordinata y: "))

#aggiorno le coordinate
punto.muovi(dx, dy)
print("Nuove coordinate:", punto.x, punto.y)      

#calcolo la distanza dall'origine
distanza = punto.distanza_da_origine()
print("Distanza dall'origine:", distanza)