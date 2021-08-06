""""7) Wygeneruj kolejne liczby Fibonacciego z przedziału [1, 100]. Pierwsze
dwie sa równe 0 i 1, nastepne powstaja poprzez obliczenie sumy dwóch
poprzednich a1 = 0, a2 = 1, an+1 = an−1 + an."""

n = int(input("Podaj liczbe: "))

def fib(n):
    if n==0:
        fibonacci = 0
    elif n==1:
        fibonnaci = 1
    elif n>1:
        wynik=0
        fibonnaci = [0,1]
        for i in range(1,n):
            fib1 = fibonnaci[-2]
            fib2 = fibonnaci[-1]
            fib=fib1+fib2
            fibonnaci.append(fib)
    return fibonnaci

print(fib(n))




