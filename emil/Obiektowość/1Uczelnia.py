'''1. Zaimplementowac i przetestowac hierarchie składajaca sie z nastepujacych
klas: Osoba, Student, Wykładowca oraz Stypendysta. Poszczególne
klasy zawieraja nastepujace cechy:
 Osoba: imie, nazwisko, pesel, rok urodzenia oraz płec
 Student: zawiera wszystkie cechy zawarte w klasie Osoba oraz numer
indeksu
 Wykładowca: zawiera wszystkie cechy zawarte w klasie Osoba oraz
tytuł (tytuł naukowy lub stopien naukowy)
 Stypendysta: zawiera wszystkie cechy zawarte w klasie Student
oraz kwote stypendium.
Kazda klasa powinna równiez zawierac: zestaw funkcji umozliwiajacych
nadac wartosci poczatkowe, odczyt odpowiednich pól.'''

class Osoba():
    def __init__(self,imie,nazwisko,pesel,rok_urodzenia,plec):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.rok = rok_urodzenia
        self.plec = plec

    @property
    def name(self):
        return self.imie

    @property
    def surname(self):
        return self.nazwisko

    @property
    def pes(self):
        return self.pesel

    @property
    def urodziny(self):
        return self.rok_urodzenia

    @property
    def pl(self):
        return self.plec

    @name.setter
    def name(self,name):
        self.imie = name

    @surname.setter
    def surname(self,surname):
        self.nazwisko = surname

    @pes.setter
    def pes(self,nr):
        self.pesel = nr

    @urodziny.setter
    def urodziny(self,rok):
        self.rok_urodzenia = rok

    @pl.setter
    def pl(self,pl):
        self.plec = pl

    @name.getter
    def name(self):
        return 'Imie: ' + self.imie

    @surname.getter
    def surname(self):
        return 'Nazwisko: ' + self.nazwisko

    @pes.getter
    def pes(self):
        return 'Twoj pesel to: ',self.pesel

    @urodziny.getter
    def urodziny(self):
        return 'Twoja data urodzenia to: ',self.rok_urodzenia

    @pl.getter
    def pl(self):
        return 'Plec: ',self.plec




class Student(Osoba):
    def __init__(self,imie,nazwisko,pesel,rok_urodzenia,plec,nr_indexu):
        super().__init__(imie,nazwisko,pesel,rok_urodzenia,plec)
        self.nr_indexu = nr_indexu

    @property
    def index(self):
        return self.nr_indexu

    @index.setter
    def index(self,nr):
        self.nr_indexu = nr

    @index.getter
    def index(self):
        return self.nr_indexu

class Wykladowca(Osoba):
    def __init__(self,imie,nazwisko,pesel,rok_urodzenia,plec,tytul):
        super().__init__(imie,nazwisko,pesel,rok_urodzenia,plec)
        self.tytul = tytul

    @property
    def title(self):
        return self.tytul

    @title.setter
    def title(self,tit):
        self.tytul = tit

    @title.getter
    def title(self):
        return self.tytul

class Stypendysta(Osoba):
    def __init__(self,imie,nazwisko,pesel,rok_urodzenia,plec,kwota_stypendium):
        super().__init__(imie,nazwisko,pesel,rok_urodzenia,plec)
        self.kwota_stypendium = kwota_stypendium

    @property
    def kwota(self):
        return self.kwota_stypendium

    @kwota.setter
    def kwota(self,amound):
        self.kwota_stypendium = amound

    @kwota.getter
    def kwota(self):
        return self.kwota_stypendium


os = Osoba('jarek','jak',8888,9999,'M')
os.surname = 'ktos'
print(os.nazwisko)
print(os.__dict__)

st=Student('dadsa','yyyy',0000,8888,'M',130)
st.nr_indexu = 101
st.name = 'Git'
print(st.name)
print(st.__dict__)
print(st.nr_indexu)

wyk = Wykladowca('llll','wykladowca',9989898,2999,'M','MGR')
wyk.name = 'Tom'
print(wyk.name)

styp = Stypendysta('ala','kota',8787,2020,'M',999)
styp.name = 'Jane'
print(styp.name)
print(styp.__dict__)

