tablica = [8,2,1,9,5]

# def insertSort(tab):
#     i = 1
#     while i < len(tab):
#         key = tab[i]
#         j = i - 1
#         while j >= 0 and key < tab[j]:
#             tab[j+1] = tab[j]
#             j-=1
#         tab[j + 1] = key
#         i+=1
#         print(tab)
#
# print(insertSort(tablica))

def insertionRekurencyjnie(tab,n):

    if n == 0:
        return None
    else:
        insertionRekurencyjnie(tab,n-1)
        ostatni = tab[n-1]
    print(ostatni)
    i = j = 0
    if ostatni > tab[i]:
        tab[i], ostatni = ostatni, tab[i]
        j+=1
        i+=1
    else:

    # else:
    #     tab[j] = ostatni
    #     j+=1
        print(tab)

    # i = 0
    # while i < len(tab):
    #     j = i + 1
    #     while



print(insertionRekurencyjnie(tablica, len(tablica)))
