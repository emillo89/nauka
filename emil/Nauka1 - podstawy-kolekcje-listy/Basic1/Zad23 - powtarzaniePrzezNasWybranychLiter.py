def tnij_do(str,n):
    length = 2
    if length > len(str):
        length = len(str)

    text = str[:length]
    wynik = ''

    for i in range(n):
        wynik = wynik + text
    return wynik
print(tnij_do('adaqeeqewq',4))