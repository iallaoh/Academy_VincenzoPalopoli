#1
num=int(input('inserisci un numero: '))
X=True
while X==True:
    num=int(input('inserisci un numero: '))
    if num%2==0:
        print('Pari')
    else:
        print('Dispari')
    scelta=input('vuoi ripetere con un altro numero? s/n: ')
    if scelta=='s':
        num=int(input('inserisci un nuovo numero: '))
    else:
        print('stop')
        X=False
    
    
#2
num=int(input('inserisci un numero: '))
X=True
while X==True:
    for i in range(num, -1, -1):
        print (i)
    scelta=input('vuoi ripetere con un altro numero? s/n: ')
    if scelta=='s':
        num=int(input('inserisci un nuovo numero: '))
    else:
        print('stop')
        break
    
#3
lista=[]
numeri=int(input('quanti numeri vuoi nella lista? '))
for i in range(0, numeri, 1):
    num=int(input('inserisci numero: '))
    lista.insert(i, num)
for i in lista:
    print(i**2)
    
#4
lista=[]
numeri=int(input('quanti numeri vuoi nella lista? '))
for i in range(0, numeri, 1):
    num=int(input('inserisci numero: '))
    lista.insert(i, num)
#massimo
lista.sort()
max=lista[len(lista)-1]
print(f"il numero massimo è {max}")
#conteggio
count=0
while count!=len(lista):
    count=count+1
print(count)

#
if count==0:
    print('lista vuota')
else:
    print(f"il numero massimo è {max} e ci sono {count} numeri")
    









