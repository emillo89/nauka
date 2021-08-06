cyf = input("podaj cyfre,ktora chcesz wyswietlic slownie")
liczby ={'0':'zero','1':'jeden','2':"dwa",'3':'trzy','4':'cztery', '5':'piec','6':'szesc','7':'siedem', '8':'osiem','9':'dziewiec'}

def cyfra(ile):
    lista = []
    ciag = ''
    for i in ile:
        lista.append(i)
    if int(ile) == 0:
        # print('zero')
        ciag +='zero'
    elif int(ile) < 0:
        ciag +='minus '
        for i in lista:
            if i in liczby.keys():
                # print(liczby[i])
                ciag+=liczby[i]+" "
    elif int(ile) > 0 :
        for i in lista:
            if i in liczby.keys():
                # print(liczby[i])
                ciag +=liczby[i] +" "
    return ciag

print(cyfra(cyf))









