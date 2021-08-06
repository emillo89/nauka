class Czlowiek():
    imie = 'Sebastian'
    wiek = 30
    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek = wiek


    def przewitaj(self,przewitaj = 'Witam'):
        return przewitaj+ ' mam na imie '+self.imie + " i lat"+ str(self.wiek)

obiekt = Czlowiek('Marek',25)

print(obiekt.przewitaj())
