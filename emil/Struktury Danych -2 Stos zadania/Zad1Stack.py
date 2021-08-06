class Stack():
    def __init__(self,size):
        self.stack = []
        self.size = size

    def push(self, item):
        if self.size == len(self.stack):
            print('stack is full')
        else:
            self.stack.append(item)

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

    def peek(self):
        if self.stack == []:
            raise Exception ('stos jest pusty')
        else:
            return self.stack[len(self.stack)-1]
    def display(self):
        if self.stack == []:
            print('stack jest pusty')
        else:
            print('stack data')
            for item in reversed(self.stack):
                print(item)

stos = Stack(5)
stos.push(10)
stos.push(17)
stos.push(56)
stos.push(88)
stos.display()
print('----')
stos.push_start(22)
stos.display()

