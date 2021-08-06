wysokosc = int(input("Podaj wysokosc choinki"))


def rysuj(wysokosc):
    line = '*'
    for i in range(wysokosc):
        print(line.center(10))
        line = line + '**'
# print('*'.center(80, ' '))  - ta linia pozwoli nam na to ze bedziemy miec pieniek choinki

rysuj(wysokosc)



