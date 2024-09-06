def primo_o_no(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False, i  #restituisce False e il divisore più piccolo
    return True, None  #restituisce True se è primo e None come divisore

#chiedo nome e il numero all'utente
nome = input("Inserisci il tuo nome: ")
numero = int(input("Inserisci un numero: "))

#verifico se il numero è primo
primo, divisore = primo_o_no(numero)

if primo==True:
    print(f"Ciao {nome}, il numero {numero} è primo!")
else:
    print(f"Ciao {nome}, il numero {numero} non è primo. Il divisore più piccolo è {divisore}.")
