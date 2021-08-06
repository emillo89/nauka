class Odwroc():
    def __init__(self,dane):
        self.dane = dane
        self.indeks = len(dane)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indeks == 0:
            raise StopIteration

        self.indeks -= 1
        return self.dane[self.indeks]

for i in Odwroc('Martusia'):
    print(i,end = '')

