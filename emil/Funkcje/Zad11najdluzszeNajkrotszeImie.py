"""Utwórz liste imion osób z Twojej grupy, a nastepnie wypisz najdłuzsze,
najkrótsze imie. Posortuj liste. Program nie uwzglednia wielkosci liter
oraz usuwa wpisane przypadkowo spacje (funkcje upper i split)

"   tekst".lstrip()  # usuwanie znaków białych z lewej strony
'tekst'
"tekst   ".rstrip()  # usuwanie znaków białych z prawej strony
'tekst'
"   tekst       ".strip()  # usuwanie znaków białych z obu stron
'tekst'

---nie wiem jak usunac wczesniej dodane???????????? oraz sortowanie?????
"""

lista2 = [' Jacek','Maciek','Wojtek','Zbyszek',"Ewa",'Mariusz','Ola','Kajtek']

lista2.sort()
print(lista2)

def min_max(list):
    list.sort()
    lista = []
    # usuniecie spacji i zamiana na male litery
    for j in lista2:
        lista.append(j.strip().lower())
    j = len(lista)


    while j>0:
        len_min = 3
        len_max = 0
        word_min = ''
        word_max = ''
        list_min= []
        list_max = []
        # dodanie do listy imion najdluzszych/krotszych, jednak jesli cos jest dluzsze/krotsze od poprzedniego to nie usuwa poprzednika
        for i in lista:
            if len_min>= len(i):
                word_min = i
                len_min=len(i)
                list_min.append(i)

            elif len_max <= len(i):
                word_max = i
                len_max = len(i)
                if len_max == len(i):
                    list_max.append(i)
        j-=1
        # wybranie najdluzszych i najkrotszych imion
    min = []
    max = []
    for l in list_min:
        if len(l) == len_min:
            min.append(l)
    for l in list_max:
        if len(l) == len_max:
            max.append(l)



    print('max: ',list_max, ',word min: ',list_min)
    print('word min: ',min, ',word max: ',max)

min_max(lista2)





