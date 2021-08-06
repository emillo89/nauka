class Pojazd():
    def __init__(self,imie_wlasciciela,nazwisko_wlasciciela,
                 adres_wlasciciela,marka_pojazdu,model_pojazdu,nr_rej,
                 rodzaj_nadwozia,kolor_pojazdu,nr_vin,masa_wlasna,
                 dop_ladownosc,liczba_miejsc,pojemnosc_silnika,
                 rok_produkcji,data_rejestracji,next_badanie_techniczne):
        self.imie_wlasciciela = imie_wlasciciela
        self.nazwisko_wlasciciela = nazwisko_wlasciciela
        self.adres_wlasciciela = adres_wlasciciela
        self.marka_pojazdu = marka_pojazdu
        self.model_pojazdu = model_pojazdu
        self.nr_rej = nr_rej
        self.rodzaj_nadwozia = rodzaj_nadwozia
        self.kolor_pojazdu  = kolor_pojazdu
        self.nr_vin = nr_vin
        self.masa_wlasna = masa_wlasna
        self.dop_ladownosc = dop_ladownosc
        self.liczba_miejsc = liczba_miejsc
        self.pojemnosc_silnika = pojemnosc_silnika
        self.rok_produkcji = rok_produkcji
        self.data_rejestracji = data_rejestracji
        self.next_badanie_techniczne = next_badanie_techniczne

    #1 wlasciwosci

    @property
    def imie(self):
        return self.imie_wlasciciela

    @property
    def nazwisko(self):
        return self.nazwisko_wlasciciela

    @property
    def adres(self):
        return self.adres_wlasciciela

    @property
    def marka(self):
        return self.marka_pojazdu

    @property
    def model(self):
        return self.model_pojazdu

    @property
    def rej(self):
        return self.nr_rej

    @property
    def nadwozie(self):
        return self.rodzaj_nadwozia

    @property
    def kolor(self):
        return self.kolor_pojazdu

    @property
    def vin(self):
        return self.nr_vin

    @property
    def masaW(self):
        return self.masa_wlasna

    @property
    def ladownosc(self):
        return self.dop_ladownosc

    @property
    def miejsc(self):
        return self.liczba_miejsc

    @property
    def poj_silnika(self):
        return self.pojemnosc_silnika

    @property
    def rok_prod(self):
        return self.rok_produkcji

    @property
    def rejestracja(self):
        return self.data_rejestracji

    @property
    def nast_badanie(self):
        return self.next_badanie_techniczne

    #2 gettery

    @imie.getter
    def imie(self):
        return 'Imie: ' + self.imie_wlasciciela

    @nazwisko.getter
    def nazwisko(self):
        return 'Nazwisko: ' + self.nazwisko_wlasciciela

    @adres.getter
    def adres(self):
        return 'Adres: ' + self.adres_wlasciciela

    @marka.getter
    def marka(self):
        return 'Marka pojazdu: ' + self.marka_pojazdu

    @model.getter
    def model(self):
        return 'Model pojazdu: ' + self.model_pojazdu

    @rej.getter
    def rej(self):
        return 'Nr dowodu rejestracyjnego: ' + self.nr_rej

    @nadwozie.getter
    def nadwozie(self):
        return 'Typ nadwozia: ' + self.rodzaj_nadwozia

    @kolor.getter
    def kolor(self):
        return 'Kolor pojazdu: ' + self.kolor_pojazdu

    @vin.getter
    def vin(self):
        return 'Nr vin: ' + self.nr_vin

    @masaW.getter
    def masaW(self):
        return 'Masa wlasna pojazdu: ' + self.masa_wlasna

    @ladownosc.getter
    def ladownosc(self):
        return 'Ladnosc pojazdu wynosi: ' + self.dop_ladownosc

    @miejsc.getter
    def miejsc(self):
        return 'Liczba miejsc w pojazdzie: ' + self.liczba_miejsc

    @poj_silnika.getter
    def poj_silnika(self):
        return 'Pojemnosci silnika: ' + self.pojemnosc_silnika

    @rok_prod.getter
    def rok_prod(self):
        return 'Rok produkcji' + self.rok_produkcji

    @rejestracja.getter
    def rejestracja(self):
        return 'Data rejestracji pojazdu" ' + self.data_rejestracji

    @nast_badanie.getter
    def nast_badanie(self):
        return 'Data nastepnego badania technicznego: ' + self.next_badanie_techniczne

    #3 settery

    @imie.setter
    def imie(self,name):
        self.imie_wlasciciela = name

    @nazwisko.setter
    def nazwisko(self,surname):
        self.nazwisko_wlasciciela = surname

    @adres.setter
    def adres(self,adress):
        self.adres_wlasciciela = adress

    @marka.setter
    def marka(self,brand):
        self.marka_pojazdu = brand

    @model.setter
    def model(self,mod):
        self.model_pojazdu = mod

    @rej.setter
    def rej(self,nr):
        self.nr_rej = nr

    @nadwozie.setter
    def nadwozie(self,body):
        self.rodzaj_nadwozia = body

    @kolor.setter
    def kolor(self,color):
        self.kolor_pojazdu = color

    @vin.setter
    def vin(self,nr):
        self.nr_vin = nr

    @masaW.setter
    def masaW(self, mass):
        self.masa_wlasna = mass

    @ladownosc.setter
    def ladownosc(self,weight):
        self.dop_ladownosc = weight

    @miejsc.setter
    def miejsc(self,place):
        self.liczba_miejsc = place

    @poj_silnika.setter
    def poj_silnika(self,capacity):
        self.pojemnosc_silnika = capacity

    @rok_prod.setter
    def rok_prod(self,year):
        self.rok_produkcji = year

    @rejestracja.setter
    def rejestracja(self,register):
        self.data_rejestracji = register

    @nast_badanie.setter
    def nast_badanie(self,next):
        self.next_badanie_techniczne = next

    #4 wypisz

    def wypisz_imie(self):
        return 'Imie: ' + self.imie_wlasciciela

    def wypisz_nazwisko(self):
        return 'Nazwisko: ' + self.nazwisko_wlasciciela

    def wypisz_adres(self):
        return 'Adres: ' + self.adres_wlasciciela

    def wypisz_marka(self):
        return 'Marka pojazdu: ' + self.marka_pojazdu

    def wypisz_model(self):
        return 'Model pojazdu: ' + self.model_pojazdu

    def wypisz_rej(self):
        return 'Nr dowodu rejestracyjnego: ' + self.nr_rej

    def wypisz_nadwozie(self):
        return 'Typ nadwozia: ' + self.rodzaj_nadwozia

    def wypisz_kolor(self):
        return 'Kolor pojazdu: ' + self.kolor_pojazdu

    def wypisz_vin(self):
        return 'Nr vin: ' + self.nr_vin

    def wypisz_masaW(self):
        return 'Masa wlasna pojazdu: ' + self.masa_wlasna

    def wypisz_ladownosc(self):
        return 'Ladnosc pojazdu wynosi: ' + self.dop_ladownosc

    def wypisz_miejsc(self):
        return 'Liczba miejsc w pojazdzie: ' + self.liczba_miejsc

    def wypisz_poj_silnika(self):
        return 'Pojemnosci silnika: ' + self.pojemnosc_silnika

    def wypisz_rok_prod(self):
        return 'Rok produkcji' + self.rok_produkcji

    def wypisz_rejestracja(self):
        return 'Data rejestracji pojazdu" ' + self.data_rejestracji

    def wypisz_nast_badanie(self):
        return 'Data nastepnego badania technicznego: ' + self.next_badanie_techniczne



class Lodz():
    def __init__(self):
        pass


class Amfibia(Pojazd,Lodz):
    def __init__(self,imie_wlasciciela,nazwisko_wlasciciela,
                 adres_wlasciciela,marka_pojazdu,model_pojazdu,nr_rej,
                 rodzaj_nadwozia,kolor_pojazdu,nr_vin,masa_wlasna,
                 dop_ladownosc,liczba_miejsc,pojemnosc_silnika,
                 rok_produkcji,data_rejestracji,next_badanie_techniczne):
        super().__init__(imie_wlasciciela,nazwisko_wlasciciela,
                 adres_wlasciciela,marka_pojazdu,model_pojazdu,nr_rej,
                 rodzaj_nadwozia,kolor_pojazdu,nr_vin,masa_wlasna,
                 dop_ladownosc,liczba_miejsc,pojemnosc_silnika,
                 rok_produkcji,data_rejestracji,next_badanie_techniczne)



poj = Pojazd('Jacek','Placek','Polska','Toyota','Yaris','WND 5555','sedan','red',
              'PPP0900yy','500','1000','5','2',2010,2019,2022)

print(poj.__dict__)
# poj.imie = 'Radek'
print(poj.imie)

print(poj.imie_wlasciciela)


amf = Amfibia('Jacek','Placek','Polska','Toyota','Yaris','WND 5555','sedan','red',
              'PPP0900yy','500','1000','5','2',2010,2019,2022)

print(amf.data_rejestracji)
print(amf.imie_wlasciciela)
amf.imie = 'Tomek'
print(amf.imie)
print(amf.imie_wlasciciela)
print(amf.__dict__)
amf.imie_wlasciciela = 'Rysio'
print(amf.__dict__)
print(amf.wypisz_rej())