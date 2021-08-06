tablica = [1,2,5,8,9]
tablica.sort()
print(tablica)

def binarne(tab, low, high, szukana):
    mid = (low+high)//2

    if szukana not in tab:
        return None
    else:
        if szukana == tab[mid]:
            return mid,tab[mid]
        elif szukana> tab[mid]:
            return binarne(tab, mid+1,high, szukana)
        elif szukana < tab[mid]:
            return binarne(tab,low, mid-1,szukana)
print(binarne(tablica,0,len(tablica) -1,2))