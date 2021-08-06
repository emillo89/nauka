class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False


    def push(self,data):
        new = Node(data)
        if self.head == None:
            self.head = new
        else:
            new.next = self.head
            self.head = new
    def pop(self):
        if self.isEmpty():
            return None
        else:
            tmp = self.head
            self.head = self.head.next
            tmp.next = None
            return tmp.data

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
    def display(self):
        iter = self.head
        if self.isEmpty():
            print('lista jest pusta')
        else:
            while iter != None:
                print(iter.data,end = '\n')
                iter = iter.next
            return



q = Stack()
q.push('5')
q.push('10')
q.push('14')
q.push('1')

print('----')

q.pop()
q.display()
print('----')
print(q.peek())


