from math import sqrt, degrees, atan2


class Wektor:
    # inicjalizowanie obiektu
    def __init__(self,x = 0.0,y = 0.0):
        '''self.x - odnosi sie do atrybutu,czyli dana jaka bedzie
        przechowywal obiekt w momencie stworzenia
        x - jaka dana zostanie mu przekazana'''

        self.x = x
        self.y = y

    # aby dla obiektów działał +
    def __add__(self, other):
        return Wektor(self.x + other.x, self.y + other.y)

    # aby dla obiektów działał +=
    def __isadd__(self,other):
        self.x += other.x
        self.y += other.y
        return self

    # aby dla obiektów działał -
    def __sub__(self, other):
        return Wektor(self.x - other.x, self.y - other.y)

    # aby dla obiektow dzialal *
    def __mul__(self, other):
        return Wektor(self.x * other.x, self.y * other.y)

    # aby dla obiektow dzialal /
    def __div__(self, other):
        return Wektor(self.x / other.x, self.y - other.y)

    # dlugosc wektora
    def dlugosc(self):
        return sqrt(self.x**2 + self.y**2)

    # czy wektor 1 jest krotszy niz 2
    def __lt__(self, other):
        return self.dlugosc() < other.dlugosc()

    # czy wektor 1 jest dluzszy niz wektor 2
    def __gt__(self, other):
        return self.dlugosc() > other.dlugosc()

    # czy wektory sa sobie rowne
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # kat
    def kat(self):
        return degrees(atan2(self.y, self.x))

    # informacje
    def wyswietl(self):
        return ' Wspolrzedna x: ' + str(self.x) + 'wspolrzedna y: ' + str(self.y) +'''
        dlugosc wektora: ''' + str(self.dlugosc()) + 'kat wektora' + str(self.kat())
wektor1 = Wektor(2,5)
wektor2 = Wektor(5,10)
print(wektor1.x)
print(wektor2.x)
wektor3 = wektor1 + wektor2
print(wektor3.x)
print(wektor3.y)
wektor3+=wektor2
print(wektor3.x)
print(wektor3.y)
wektor4 = wektor3 - wektor1
print(wektor4.x)

print('wektor4',wektor4.wyswietl())
print(wektor1.dlugosc())
print(wektor2.dlugosc())
print(wektor1 < wektor2)
print(wektor1 > wektor2)
print(wektor1 > wektor2)
print(wektor1 == wektor2)
