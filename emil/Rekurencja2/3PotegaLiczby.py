'''3. Napisz algorytm wyznnaczjacy potege danej liczby.'''

def potega_rekurencyjnie(a,n):
    if n == 0:
        return 1
    elif n > 0:
        return a*potega_rekurencyjnie(a,n-1)
print(potega_rekurencyjnie(3,2))
