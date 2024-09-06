#genera numero casuale tra 1 e 100
import random
numero_casuale = random.randint(1, 100)

def indovina_numero(numero):
    if numero<numero_casuale:
        print("il numero che hai scelto è minore")
    elif numero>numero_casuale:
        print("il numero che hai scelto è maggiore")
    else:
        print("hai indovinato!")
        return False
   

while True:
         numero=int(input("indovina il numero: "))
         indovina_numero(numero)


    




