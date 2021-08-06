import re

wynik = re.match(r'^Hello World$', 'Hello World')

if wynik:
    print('dopasowano')
else:
    print('nie dopasowano')