tablica = [8,2,1,9,5]
print(tablica)

def selectionSort(tab):
    i = 0
    while i < len(tab) - 1 :
        minIndex = i
        j = i + 1
        while j < len(tab):
            if tab[minIndex] > tab[j]:
                minIndex = j
            j +=1
        tab[minIndex],tab[i] = tab[i],tab[minIndex]
        i += 1
        print(tab)

selectionSort(tablica)
