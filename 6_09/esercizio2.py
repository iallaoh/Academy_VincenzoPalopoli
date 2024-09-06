#fibonacci
def fibonacci_ricorsivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_ricorsivo(n-1) + fibonacci_ricorsivo(n-2)

n=int(input("inserisci un numero: "))

for i in range(n):
    fibonacci_ricorsivo(i)