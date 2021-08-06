from collections import defaultdict


class Stack():
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.dict = {}

    def push(self, item):
        if self.size == len(self.stack):
            print('stack is full')
        else:
            for i in item:
                if i in '()':
                    self.stack.append(i)
                else:
                    print('NIE')
                    self.stack.clear()
                    return

    def push_start(self, item):
        if self.size == len(self.stack):
            print('stack is full')
        else:
            self.stack.insert(0, item)

    def pop(self):
        if self.size == 0:
            return 'lista jest pusta'
        else:
            return self.stack.pop()

    def sprawdz(self):

        for i, j in enumerate(self.stack):
            if self.stack[i] =='(' and self.stack[i+1] == ')':
                self.add_dict(i+1,i+2)
                print(i,self.stack.pop (i))
                print(i,self.stack.pop(i))
        if len(self.stack) > 0:
            print('cos nie tak, slownik nie doda mi powtorzen oraz jak zrobic zeby ')
            self.sprawdz()

        return self.dict

    def add_dict(self,i,j):
        self.dict[i] = j
    def peek(self):
        if self.stack == []:
            raise Exception('stos jest pusty')
        else:
            return self.stack[len(self.stack) - 1]

    def display(self):
        if self.stack == []:
            print('stack jest pusty')
        else:
            print('stack data')
            for item in self.stack:
                print(item, end='')


stos = Stack(2000000)
stos.push('()(()(()))')
stos.display()
print('\n----')
print(stos.sprawdz())
print(stos.stack)

# lista = ['(', ')', '(','(']
#
# for i in lista:
#     print(lista[i])


