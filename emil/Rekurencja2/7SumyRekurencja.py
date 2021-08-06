'''7. Napisac funkcje która oblicza nastepujaco zdefiniowane sumy:'''

# 1

def suma1(n):

    if n == 1:
        return 1
    elif n>0:
        return float(1/n) + float(suma1(n-1))


print(suma1(4))


# 2

def suma2(n):
    if n==1:
        return 1
    elif n>1:
        return float(1/pow(n,2)) + suma2(n-1)


print(suma2(4))

# 3

def suma3(n):
    if n==1:
        return 1
    elif n>1:
        return n + suma3(n-1)

print(suma3(4))

# 4

def potega(n):
    if n==0:
        return 1
    elif n == 1:
        return 2
    elif n>0:
        return 2*potega(n-1)

print(potega(4))

# 5

def suma5(n):
    if n==1:
        return 1
    elif n>1:
        return n*suma5()