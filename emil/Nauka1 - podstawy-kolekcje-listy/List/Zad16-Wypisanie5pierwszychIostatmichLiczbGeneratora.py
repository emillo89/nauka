def generator():
    lista = []
    for i in range(1,21):
        lista.append(i**2)
    print(lista[:5])
    print(lista[-5:])

generator()