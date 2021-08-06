"""5. Masz dane liste panstw i liste odpowiadajacych im miast (stolic). Zaproponuj
strukture danych i napisz program - gre w której losujemy jedno
panstwo i oczekujemy podania jego stolicy. Program powinien miec
mozliwosc dodania nowego panstwa i jego stolicy, zliczania punktów
i informwania gracza o jego wyniku. Grcz decyduje o ilosci powtórzen."""
import random

# panstwa = ['Polska','Rosja','Niemcy','Czechy','Slowacja','Litwa','Ukraina','Bialorus']
panstwa = ['Polska','Rosja']
stolice = ['Warszawa','Moskwa','Berlin','Praga','Bratyslawa','Wilno','Kijow','Minsk']

slownik = {}

for i,j in zip(panstwa,stolice):
    # print(i,j)
    slownik[i]=j

# print(slownik)

def losuj():

    graj = "tak"
    pko = 0
    while (graj == "tak" or  graj != "nie") and len(panstwa)>0:
        co = int(input("""Co chcesz zrobic?
            1.Zagraj w gre.Wylosuj państwo i odpowiedz jaka jest jego stolica
            2.Dodaj nowe panstwo i stolice
            3.Pokaz punkty(prawidlowe odpowiedzi sa zliczone)\n"""))
        if co == 1:
            k = random.choice(panstwa)
            print(k)
            pytanie =input("Podaj stolice danego Panstwa:\n")

            if pytanie.strip().lower() == slownik[k].lower():
                print( pytanie.upper() + " jest stolica " + k)
                pko += 1
                panstwa.remove(k)
            else:
                print( pytanie.upper() + "nie jest stolica " + k)

        elif co == 2:
            panstwo = input("Podaj panstwo, ktore chcesz dodac: ")
            stolica = input("Podaj stolice tego panstwa: ")
            if panstwo != slownik.keys():
                slownik[panstwo] = stolica
                panstwa.append(panstwo)
        elif co == 3:
            print(pko)




        graj = input("Czy chcesz grac dalej? tak/nie")
        print(panstwa)
    # nie wiem jak zrobic zeby wyswietlilo nam pkt jezeli lista jest pusta
    if len(panstwa) == 0:
        print('punkty: ',pko)


losuj()

