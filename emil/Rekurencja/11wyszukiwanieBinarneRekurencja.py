'''11. Napisz algorytm (z wykorzystaniem rekurencji) wyszukiwania binarnego klucza key w posortowanej rosnąco liście A.
Jeżeli klucz key znajduje się w liście A, to algorytm powinien
zwrócić taki indeks k, że A[k] = key. Jeżeli klucz key nie znajduje się w liście A, to algorytm
powinien zwrócić None.
Jaka jest wg Ciebie złożoność czasowa optymistyczna i pesymistyczna podanego algorytmu?'''

tablica = [8,2,1,9,5]
tablica.sort()
print(tablica)

def binarne(tab, low, high, szukana):

    mid = (high + low) // 2

    if szukana not in tab:
        return None

    else:
        if tab[mid] == szukana:
            return mid, tab[mid] , szukana
        elif tab[mid] > szukana:
            return binarne(tab, low, mid - 1, szukana)
        elif tab[mid] < szukana:
            return binarne(tab, mid + 1, high, szukana)


print(binarne(tablica,0,len(tablica) - 1, 2))
