numeri_primi = []
contatore_primi = 0

while contatore_primi < 5:
    numero = int(input("Inserisci un numero: "))

    # Controllo se il numero è primo
    if numero <= 1:
        print(numero, "non è un numero primo.")
    else:
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                print(numero, "non è un numero primo.")
                break
        else:
            numeri_primi.append(numero)
            contatore_primi += 1
            print(numero, "è un numero primo.")

print("Hai inserito 5 numeri primi!")
print("I numeri primi sono:", numeri_primi)