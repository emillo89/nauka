'''
9. Zaimplementuj rekurencyjną wersję algorytmu Euklidesa obliczającego największy wspólny
dzielnik dwóch liczb naturalnych.
'''

def algorytm(a,b):
    if b == 0:
        return a
    else:
        reszta = a%b
        a,b = b,reszta
        return algorytm(a,b)




print(algorytm(1000,500))