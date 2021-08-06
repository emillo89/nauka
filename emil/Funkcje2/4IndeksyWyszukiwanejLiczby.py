"""Napisz funkcje zwaracjaca indeksy elementów sposród 20 elementów
losowo wygenerowanej tablicy równych wyszukiwanej wartosci."""
import random


def wyszukiwanie_indexu(x):
    lista = []
    j=0
    while j<=20:
        k = random.randint(1,200)
        lista.append(k)
        j+=1
    lista.sort
    for i in range(len(lista)):
        if lista[i] == x:
            print(i,lista) # wyszukuje nam na ktorej iteracji jest liczba = 12
            continue

            # return  i
    return -1

wyszukiwanie_indexu(12)