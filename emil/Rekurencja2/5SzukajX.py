"""5. Zaprojektowac algorytm, rozwiazujacy problem poszukiwania zadanej
liczby x w tablicy, która jest posortowana od wartosci minimalnych do
maksymalnych."""

tablica = [4,12,7,19,22]

def szukaj(tab,x):

    tab.sort(reverse=False)
    if tab[0] == x:
        return x
    else:
        tab.pop(0)
        return szukaj(tab,x)


print(szukaj(tablica,22))

#  lub 2 sposob zapisu
tablica = [4,12,7,19,22]

def szukaj(tab, x):
    tab.sort()
    if tab[0] == x:
        print('{} został znaleziony'.format(x))
    else:
        print(tab)
        return szukaj(tab[1:],x)


print(szukaj(tablica,12))