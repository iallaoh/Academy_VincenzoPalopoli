def uml():
    print(f"uml, acronimo di {"unified modeling language"}, è un linguaggio che permette di rappresentare in maniera visiva e fortemente standardizzata, attraverso diagrammi, il flusso di un sistema software.")

def lista():
    print("una lista è un contenitore ordinato di variabili di qualsiasi tipo")
    print("ecco un esempio di lista")
    lista_prova=["ciao", 12, True]
    return lista_prova
    
def ciclo():
    print("un ciclo è un blocco di codice che serve per ripetere delle azioni in base a determinate condizioni: while si usa quando non è definito il numero di iterazioni, al contrario si usa for")
    print("esempio con for: ")
    for i in range(5):
        print(i)
       
    print("esempio con while: ") 
    numero = 0
    while numero < 5:
        print(numero)
        numero += 1
        

def tasking():
    print("il tasking è il processo di gestione dei compiti da assegnare ai dipendenti in un progetto")
    
def range_func():
    print("il range è una funzione che permette di creare una sequenza di numeri, si può specificare l'inizio, la fine (non inclusa) e lo step ")
    print("ecco un esempio di range")
    numeri = list(range(5))
    print(numeri)
        

numeri = list(range(5,10))
print(numeri)
    