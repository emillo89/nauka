import re

if re.match(r'^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9\.-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9\.-])\.[A-Za-z0-9]+$',"ala@gmail.pl"):
    print('dopasowano')
else:
    print('Nieodpasowano')