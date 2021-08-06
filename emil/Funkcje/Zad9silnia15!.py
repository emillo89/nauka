"""9)Policz 15!, wypisz na ekranie tylko 3 pierwsze cyfry tej liczby."""
n = int(input("podaj liczbe,ktorej silnie chcesz obliczyc: "))



def silnia(n):
    trzy_liczby = []
    if n in (0,1):
        wynik = 1
        trzy_liczby.append(n)


    elif n>1:
        wynik = 1
        for i in range(1,n+1):
            wynik*=i
            trzy_liczby.append(i)
    for i in trzy_liczby:
        li=4
        while i<li:
            print("Liczby: ",i)
            break

    return str(wynik)[:3]



print(silnia(n))


