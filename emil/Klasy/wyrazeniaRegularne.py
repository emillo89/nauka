import re

text = r"gruszkajablkogruszka"
wzor = r'jablko'
zmiana = r'truskawka'

print(re.match(wzor,text))
print(re.search(wzor,text))
print(re.findall(wzor,text))
print(re.sub(wzor,zmiana,text))
# print(re.sub(zmiana,))

'''
^oznacza od poczatku
$ oznacza do konca
[Kk] - wystepowanie jednego ze z    1`  1nakow
. wszystko pozotale, chyba ze .$ oznacza to jeden znak
[^] - oznacza to ze maja nastepujace znaki nie wystapic

'''
if re.match('^[Kk]o.$', 'ko9'):
    print('dopasowano')
else:
    print('nie dopasowano')

'''
* znak moze zostac powtorzony wiele razy
+ to samo co * ale symbol musi wystąpic chociaz raz
? moze nie wystapic w ogole lub tylko raz
{}  - {min,max} min oraz max ilosc wystapien

'''

if re.match("^[A-Z][a-z]*$", "Al"):
    print("dopasowano")
else:
    print("Niedopasowano")

'''Grupowanie
() grupowanie
(?:He) - bez nazwy grupowanie
(?P<first>)
| oznacz lub
(!|\.) wykrzyknik lub kropka'''
wynik = re.match(r"^((?:He)(?P<first>ll)o)( World)+(!|\.)$", "Hello World World.")

if wynik:
    print("Dopasowano")
    print(wynik.group())
    print(wynik.group(0))
    print(wynik.group('first'))
    print(wynik.groups())
else:
    print('Niedopasowano')