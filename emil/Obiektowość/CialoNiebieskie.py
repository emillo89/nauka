'''Stwórz programu ułatwiajacy prace astronomów. Program bedzie słuzył
do opisu poszczególnych ciał niebieskich.
Klasa bazowa CialoNiebieskie, powinna zawierac informacje opisujace
dowolne ciało niebieskie (nazwa danego ciała, jego masa oraz opis).
Do klasy CialoNiebieskie nalezy dodac dwie metody, które beda zwracac
informacje o danym ciele niebieskim. Pierwsza bedzie zwracac informacje
o jego nazwie i masie, druga natomiast dodatkowo opis danego
ciała niebieskiego.
Poszczególne ciała niebieskie róznia sie cechami, które je reprezentuja.
Planety dodatkowo opisujemy przy pomocy takich cech jak: okres obiegu
wokół Słonca, czas rotacji wokół własnej osi, ile dana planeta jest
ciezsza od Ziemi.
Innym rodzajem ciała niebieskiego jest gwiazda. Gwiazde, poza nazwa,
masa i opisem, maja charakteryzowac nastepujace cechy:klasa gwiazdy
2
jest oznaczona jedna z nastepujacych liter: O, B, A, F, G, K, M, R, N,
S podklasa gwiazdy, jest oznaczona cyframi od 1 do 9, ile razy dana
gwiazda jest ciezsza od Słonca.
Zauwazmy, ze łatwo zainicjalizowac własciwosc PodklasaGwiazdy niepoprawna
wartoscia. Chcac temu zapobiec, zdefiniuj własna klase reprezentujaca
wyjatek. Wyjatek bedzie zgłaszany w momencie wykrycia,
próby nadania własciwosci PodklasaGwiazdy złej wartosci.'''


class Ciało_niebieskie():
    def __init__(self,nazwa_ciala,masa_ciala,opis_ciala):
        self.nazwa_ciala = nazwa_ciala
        self.masa_ciala = masa_ciala
        self.opis_ciala = opis_ciala

    def info1(self):
        return 'Nazwa ciała niebieskiego to: ' + self.nazwa_ciala + '. Jego masa wynosi: ' + self.masa_ciala

    def info2(self):
        return 'Nazwa ciała niebieskiego to: ' + self.nazwa_ciala + '. Jego masa wynosi: ' + self.masa_ciala +'. Dodatkowo '+ self.nazwa_ciala + ' jest: ' + self.opis_ciala


cialo = Ciało_niebieskie('Ziemia','1kg','planeta')

print(cialo.info1())
print(cialo.info2())

class Planety(Ciało_niebieskie):
    def __init__(self,nazwa_ciala,masa_ciala,opis_ciala,obieg_Slonca,czas_rotacji,ile_ciezsza_od_ziemi):
        super().__init__(nazwa_ciala,masa_ciala,opis_ciala)
        self.obieg_Slonca = obieg_Slonca
        self.czas_rotacji = czas_rotacji
        self.ile_ciezsza_od_ziemi = ile_ciezsza_od_ziemi


class Gwiazdy(Ciało_niebieskie):
    klasa = ['B','O','A','F','G','K','M','R','N','S']
    podklasa = ['1','2','3','4','5','6','7','8','9']
    def __init__(self,nazwa_ciala,masa_ciala,opis_ciala,klasa_gwiazdy,podklasa_gwiazdy,ile_x_ciezsza_od_slonca):
        super().__init__(nazwa_ciala, masa_ciala, opis_ciala)

        liczba = 0
        ilosc = 0

        #klasa
        for i in self.klasa:
            if i == klasa_gwiazdy:
                self.klasa_gwiazdy = klasa_gwiazdy
                print(i)
            elif i!= klasa_gwiazdy:

                if ilosc == len(self.klasa) - 1 and liczba == 0:
                    raise print('Klasa gwiazdy jest oznaczona jedna z liter: O,B,A,F,G,K,M,R,N,S')
                else:
                    ilosc += 1

        #podklasa

        liczba = 0
        ilosc = 0
        for i in self.podklasa:
            if i == podklasa_gwiazdy:
                self.podklasa_gwiazdy = podklasa_gwiazdy
                print(i)
            elif i!= podklasa_gwiazdy:

                if ilosc == len(self.podklasa) - 1 and liczba == 0:
                    raise print('Podklasa gwiazdy jest oznaczona jedna z cyfr: 1,2,3,4,5,6,7,8,9')
                else:
                    ilosc += 1

        self.ile_x_ciezsza_od_slonca = ile_x_ciezsza_od_slonca



gw = Gwiazdy('gwi','1000','kolor','R','8','10')
print(gw.info2())
print(gw.klasa_gwiazdy)
print(gw.podklasa_gwiazdy)