C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

def wyswietl_co(list,coIle):
    return [list[i::coIle] for i in range(coIle)]

print(wyswietl_co(C,3))