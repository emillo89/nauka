""""Napisz funkcje sprawdzajaca, ile razy dana liczba wystepuje wsród 20
elementów losowo wygenerowanej listy."""
from collections import Counter
import random


def zliczanie():
    lista = []
    j=0
    while j<=20:
        k = random.randint(1,200)
        lista.append(k)
        j+=1
    print(lista)
    lista.sort()
    for i in Counter(lista).most_common():
        print(i)

zliczanie()