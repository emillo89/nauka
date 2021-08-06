tablica = [8,2,1,9,5]

def boubleSort(tab):
    i = 0
    while i < len(tab) - 1:
        j = 0
        while j < len(tab) - 1:
            if tab[j + 1] < tab[j]:
                tab[j + 1], tab[j] = tab[j], tab[j + 1]
            j += 1
        i += 1
        print(tab)

print(boubleSort(tablica))
