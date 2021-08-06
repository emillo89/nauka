# prosty przyklad ('dada' - sprawdzana zawartosc, str - czy jest typu string)
x = isinstance('dada',str)
print(x)
# przyklad na sumach

def add_numbers(x,y):
    if not (isinstance(x,int) and isinstance(y,int)):
        raise TypeError('Musza to byc liczby typu int')
    return x+y

print(add_numbers(10, 20))