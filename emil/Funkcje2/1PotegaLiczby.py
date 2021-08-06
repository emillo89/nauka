"""
1. Napisz funkcje sprawdzajaca, czy dana liczba jest potega innej liczby
całkowitej i róznej od zera.
"""

def potega(liczba):
    lista = []
    for i in range(1,liczba+1):
        for j in range(1,1025):
            if i**liczba == j:
                lista.append(i**liczba)
                print("i**liczba= ",i," ** ", liczba, ' = ', j)
            continue
    return lista

potega(4)