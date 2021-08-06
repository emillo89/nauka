class MojIterator():
    def __init__(self,maks):
        self.x = 1
        self.max = maks
    def __iter__(self):
        return self

    def __next__(self):
        x = self.x
        if self.x > self.max:
            raise StopIteration

        self.x += 3
        return x

moj = MojIterator(20)

for i in moj:
    print(i)