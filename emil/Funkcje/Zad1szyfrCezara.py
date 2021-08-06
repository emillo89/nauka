"""1)Korzystajac z informacji na temat szyfru Cezara odszyfruj napis i znjadz
wartosc przesuniecia: napis = ”Rmgi$ heg% ”"""

# otrzymanie jaki kod ASCII zostal przyporzadkowany danemu znakowi
print(ord('a'))

# otrzymanie jaki znak zostal przyporzadkowany danemu kodowi ASCII
print(chr(107))

# SZYFR CEZARA

klucz = 90

def szyfruj(text):
    zaszyfrowany = ""
    for i in range(len(text)):
        # 127 znakow czy 122?
        if ord(text[i])>127-klucz:
            zaszyfrowany+=chr(ord(text[i])+klucz-96);"""-96 bo powracamy od poczatku kody ASCII od !, lub 35 jesli od pocatku alfabetu"""
        else:
            zaszyfrowany+=chr(ord(text[i])+klucz)
    return zaszyfrowany

print(szyfruj('}'))

# deszyfrowanie textu

def deszyfruj(text):
    odszyfrowanie = ''
    key = klucz%96
    for i in range (len(text)):
        if ord(text[i]) - key < 0:
            odszyfrowanie += chr(ord(text[i]) - key + 96)

        else:
            odszyfrowanie += chr(ord(text[i]) - key)

    return odszyfrowanie

print(deszyfruj("Rmgi$ heg%"))
print(klucz%96)
print(ord("a"))


# TO JEST PRAWIDLOWE
# szyfr Cezara

klucz = 22

def deszyfruj(text):
    lista = []
    for i in range(len(text)):
        znak = ord(text[i]) - klucz
        litera = chr(znak)
        lista.append(litera.strip())
    print(lista)


deszyfruj("P01BXkgKS1YLTD0fFzwZBQxBXlxSUDNCASZGSFc5RgQDUwQlDVICKQkRXjojCBIBWBlSC0lQC0w6KE83OFhIBi09QjZWWFEjTUtdWQtMSEEtHkFVMypaPwE3RgQaNBQg")