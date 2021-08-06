def generator1(a,b):
    while a <= b:
        yield a
        a += 3

for i in generator1(2,30):
    print(i)


def odwroc(dane):
    for i in range(len(dane)-1,-1,-1):
        yield dane[i]

for i in odwroc('marta'):
    print(i,end='')