class Tunczyk():
    #tworzymy zmienna statyczna
    ilosc_tunczykow = 0

    def __init__(self,imie):
        self.imie = imie
        Tunczyk.ilosc_tunczykow += 1

    # tworzenie metody statycznej
    @staticmethod
    def getIloscTunczykow():
        print('Aktualnie liczba tunczykow to:  ', Tunczyk.ilosc_tunczykow)

    # nadpisujemy destruktor ( dokonujemy tego poniewaz jesli usuniemy jakis obiekt, to aby wskazywal
    # odpowiednia liczbe obiektow nalezy dokonac zmian, inaczej po usuniecie bedzie pokazywal ta sama liczbe obiektow

    def __del__(self):
        print('Tunczyk ', self.imie, ' zostal usuniety')
        Tunczyk.ilosc_tunczykow -= 1


Tunczyk.getIloscTunczykow()
tunczyk1 = Tunczyk('Marta')
Tunczyk.getIloscTunczykow()
tunczyk2 = Tunczyk('Emil')
Tunczyk.getIloscTunczykow()
del tunczyk2
Tunczyk.getIloscTunczykow()