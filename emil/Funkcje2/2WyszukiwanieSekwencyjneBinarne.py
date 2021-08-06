
def wyszukiwanie_binarne(x):
    lista = []
    j=0
    while j<=20:
        k = random.randint(1,20)
        lista.append(k)
        j+=1

    l = 0
    r = len(lista)

    lista.sort()
    while l <= r:
        mid = l + int((r - l) / 2)
        if lista[mid] == x:
            print(mid, lista)
            break
            # return mid
        elif lista[mid] < x:
            l = mid + 1
        else:
            r = mid
    return -1

print(wyszukiwanie_binarne(12))"""2. Napisz funkcje sprawdzajca, czy dana liczba wystepuje wsród 20 elementów
losowo wygenerowanej listy - wyszukiwanie sekwencyjne i wyszukiwanie
binarne."""

#a) wyszukiwanie liniowe - sekwencyjne
import random


# def wyszukiwanie_liniowe(x):
#     lista = []
#     j=0
#     while j<=20:
#         k = random.randint(1,200)
#         lista.append(k)
#         j+=1
#     for i in range(len(lista)):
#         if lista[i] == x:
#             print(i,lista) # wyszukuje nam na ktorej iteracji jest liczba = 12
#             # return  i
#     # return(print(lista))
#
# wyszukiwanie_liniowe(12)

# b) wyszukiwanie binarne

def wyszukiwanie_binarne(x):
    lista = []
    j=0
    while j<=20:
        k = random.randint(1,20)
        lista.append(k)
        j+=1

    l = 0
    r = len(lista)

    lista.sort()
    while l <= r:
        mid = l + int((r - l) / 2)
        if lista[mid] == x:
            print(mid, lista)
            break
            # return mid
        elif lista[mid] < x:
            l = mid + 1
        else:
            r = mid
    return -1

print(wyszukiwanie_binarne(12))


