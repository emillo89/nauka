class Stack():
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, item):
        if self.size == len(self.stack):
            print('stack is full')
        else:
            for i in item:
                if i in '{}[]()':
                    self.stack.append(i)
                else:
                    print('NIE')
                    self.stack.clear()
                    return

    def sprawdz(self):
        if len(self.stack) % 2 == 0 and len(self.stack) > 0:
            for i, j in enumerate(self.stack):
                if ((len(self.stack) - 1) // 2) >= i :
                    if j == '[':

                        k = self.stack[-1 - i]
                        if k == ']':
                            print(j, i, k)
                            continue
                        else:
                            return self.stack
                    elif j == '(':
                        k = self.stack[-1 - i]
                        if k == ')':
                            print(j, i, k)
                            continue
                        else:
                            return self.stack
                    elif j == '{':
                        k = self.stack[-1 - i]
                        if k == '}':
                            print(j, i, k)
                            continue
                        else:
                            return self.stack
                    else:
                        return self.stack

            print('TAK')
            return self.stack

        else:
            self.wrong()

    def wrong(self):
        print('NIE')
        print('zle cos')
        return self.stack


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


stos = Stack(1000)
stos.push('({})')
stos.display()
print('\n----')
print(stos.sprawdz())
print(stos.stack)