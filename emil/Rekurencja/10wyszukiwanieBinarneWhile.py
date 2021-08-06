'''10. Napisz algorytm (z wykorzystaniem pętli while) wyszukiwania binarnego klucza key w posortowanej rosnąco liście A.
 Jeżeli klucz key znajduje się w liście A, to algorytm powinien
zwrócić taki indeks k, że A[k] = key. Jeżeli klucz key nie znajduje się w liście A, to algorytm
powinien zwrócić None.'''

tablica = [8,2,1,9,5]
tablica.sort()
print(tablica)

def wyszukiwanieBinarne(tab, szukana):
    i = 0
    start = i
    end = len(tab) - 1
    mid = len(tab) // 2

    k = mid
    l = True
    if not szukana in tab:
        return None
    else:
        while l:
            if k > 0 and tab[k] > szukana:
                k -= 1

            elif k <= len(tab) and tab[k] < szukana:
                k += 1
            elif tab[k] == szukana:
                l = False
                return k, tab[k], szukana


print(wyszukiwanieBinarne(tablica,2))






