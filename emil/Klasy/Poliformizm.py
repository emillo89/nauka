'''poliformizm - uzycie meetod tej samej nazwy w różnych klasach'''\

class Ksztalt():
    def __init__(self,nazwa = 'Ksztalt'):
        self.nazwa = nazwa

    def pole(self):
        print('brak danych na temat ' + self.nazwa)


class Trojkat(Ksztalt):
    def __init__(self,nazwa = 'trojkat',a=2,h=5):
        super().__init__(nazwa)
        self.a = a
        self.h = h

    def pole(self):
        print('pole wynosi' + str((self.a *self.h )/2))

class Prostokat(Ksztalt):
    def __init__(self,nazwa = 'prostokat', a=4,b=4):
        super().__init__(nazwa)
        self.a = a
        self.b = b

    def pole(self):
        print(" pole prostokata wynosi ", self.a*self.b)

class Kwadrat():
    def __init__(self,nazwa = 'Kwadrat',a=2):
        self.nazwa = nazwa
        self.a = a

    def pole(self):
        print('pole kwadratu wynosi ',self.a**2)


ksztalt = Ksztalt()
trojkat = Trojkat()
prostokat = Prostokat()
kwadrat = Kwadrat()

lista = [ksztalt,trojkat,prostokat,kwadrat]

for x in lista:

    x.pole()