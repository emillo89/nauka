'''W jezyku Python nie da się ukryć danych, mozemy jedynie zasugerowac ze chcemy aby dane dane byly nie modyfikowane
za pomoca _ lub __ oraz możemy do tego dołączyc _klasa(jej nazwa)__ np:
'''

class Hermetyzacja:
    __lista = []

    #dodawanie argumentu do funkcji
    def dodaj(self,arg):
        self.__lista.append(arg)

    # zdejmowanie ostatniego argumentu z listy
    def zdejmij(self):
        if len(self.__lista) > 0:
            self.__lista.pop(len(self.__lista) - 1)
        else:
            print('Lista jest pusta')


obj = Hermetyzacja()
obj.dodaj('A')
obj.dodaj('B')
obj.dodaj('C')
print(obj._Hermetyzacja__lista)
obj.zdejmij()
print(obj._Hermetyzacja__lista)
obj._Hermetyzacja__lista.append('X')
print(obj._Hermetyzacja__lista)

class Ludzie(Hermetyzacja):
    pass


person = Ludzie()
print(dir(obj))
print(dir(person))

print(person._Hermetyzacja__lista)


