tablica = [8,2,1,9,5]



def mergeSort(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        L = tab[:mid]
        R = tab[mid:]
        print('L:',L); print('R:',R)
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tab[k] = L[i]
                i += 1
            else:
                tab[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tab[k] = R[j]
            j += 1
            k += 1
        print('PO',tab)

def podziel(tab,start,end):
    pivot = tab[end]
    low = start
    high = end - 1

    while True:
        while low <= high and tab[low] <= pivot:
            low += 1

        while low <= high and tab[high] >= pivot:
            high -= 1

        if low <= high:
            tab[low],tab[high] = tab[high], tab[low]
        else:
            break

    tab[end] ,tab[low] = tab[low], tab[end]
    return low

def quickSort(tab, start, end):
    if start < end:
        pivot = podziel(tab,start,end)
        quickSort(tab, start,pivot - 1)
        quickSort(tab, pivot + 1, end)
        print(tab)

print(quickSort(tablica,0, len(tablica) - 1))
print(mergeSort(tablica))
