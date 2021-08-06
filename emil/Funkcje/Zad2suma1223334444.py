"""2) Znajdz sume n liczb postaci 1 + 222 + 333 + 4444 + ....
Dla n = 4 suma = 1 + 22 + 333 + 4444
dla n = 6 suma = 1 + 22 + 333 + 4444 + 55555 + 666666"""

def sum(n):
    return (pow(10, n + 1) * (9 * n - 1) + 10) / pow(9, 3) - n * (n + 1) / 18

print(sum(3))

# za pomoca petli
def sum2(liczba):
    suma=" "
    for i in range(1,liczba+1):

        cos=(str(i)*i)

        suma += cos + " + "
    print(suma)

sum2(3)

# lub za pomoca listy
lista=[]
def sum3(liczba):
    suma=0
    for i in range(1,liczba+1):

        cos=(str(i)*i)
        lista.append(int(cos))

sum3(3)
print(lista); """lista w postaci stringa"""
suma=0
for i in lista:
    suma=suma+i
print(suma)






