"""5) Napisz program wyznaczajacy ilosc liczb w przedziale [1,100] ([1,2000])
podzielnych przez 7, które przy dzieleniu przez 2, 3, 4, 5, 6 dadza reszte
r = 1, w przypadku braku rozwiazania program powinien o tym
informowac."""

# 1 - lista
liczby = [i
    for i in range(1,303)
]
# print(liczby)

podzielne = []

def zawiera(lista):
    i=0
    count=0

    # count=0
    for i in liczby:
        if i % 7 == 0 and i % 2 == 1 and i % 3 == 1 and i % 4 == 1 and i % 5 == 1 and i % 6 == 1:
            podzielne.append(i)
            count += 1
    liczby.pop(0)
    print("Liczb podzielnych przez 7 oraz takich,ze przy dzieleniu przez 2,3,4,5,6 zostaje reszty 1 jest: ",count)
    print("liczby ktrore sa podzielne to: ",podzielne)

    if count == 0:
        print("nie ma takich liczb w danym zakresie!")

zawiera(liczby)

# 2 - lista w krotce
liczby2 = ([i
    for i in range(1,2001)
])
# print(liczby)

podzielne2 = []

def zawiera2(lista):
    i=0
    count=0

    for i in liczby2:
        if i % 7 == 0 and i % 2 == 1 and i % 3 == 1 and i % 4 == 1 and i % 5 == 1 and i % 6 == 1:
            podzielne2.append(i)
            count += 1
    krotki=liczby2.pop(0)
    print("Liczb podzielnych przez 7 oraz takich,ze przy dzieleniu przez 2,3,4,5,6 zostaje reszty 1 jest: ",count)
    print("liczby ktrore sa podzielne to: ",podzielne2)

    if count == 0:
        print("nie ma takich liczb w danym zakresie!")

zawiera2(liczby2)

