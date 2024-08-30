
X=True
while X==True:
    num=int(input('inserisci un numero: '))
    
    for i in range(num, -1, -1):
        print(i)
        risposta=input('Vuoi ripetere? s/n: ')
        if risposta=='n':
            print('stop')
            break
        X=False   

       

