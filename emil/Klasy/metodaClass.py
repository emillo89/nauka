class Czlowiek():
    def __init__(self,imie):
        self.imie = imie

    def przedstaw_sie(self):
        print("czesc mam na imie: ", self.imie)

    @classmethod
    def nowy_czlowiek(cls, imie):
        return cls(imie)

    @staticmethod
    def przywitaj(arg):
        print("czesc "+ arg)

#1. korzystanie z tworzenia obiektu
obj = Czlowiek('Seba')
print(obj.imie)
print(obj.przedstaw_sie())

#2. działanie za pomoca metody klas
object = Czlowiek.nowy_czlowiek('Artur')
print(object.przedstaw_sie())

#3. korzystanie z metody statycznej
Czlowiek.przywitaj('Przyjacielu')