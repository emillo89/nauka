tablica = [8,2,1,9,5]

def mergeSort(tablica):
    if len(tablica) > 1:
        mid = (len(tablica))//2
        L = tablica[:mid]
        R = tablica[mid:]
        mergeSort(L)
        mergeSort(R)
        print('przed L', L); print('przed R', R)

        i=j=k=0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tablica[k] = L[i]
                i+=1
                print('Lewa')
            else:
                tablica[k] = R[j]
                j+=1
                print('prawa')
            k+=1
            print('i = {} j= {} k= {}'.format(i,j,k))
            print(tablica)

        while i < len(L):
            tablica[k] = L[i]
            i+=1
            k+=1
            print('lewa lewa')
            print('i = {} k= {}'.format(i,k))
            print(tablica)

        while j < len(R):
            tablica[k] = R[j]
            j+=1
            k+=1
            print('prawa prawa')
            print('j= {} k= {}'.format(j, k))
            print(tablica)

        print('po',tablica)

mergeSort(tablica)
print(tablica)


