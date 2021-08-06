class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Quene():
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    #  dodanie do kolejki
    def EnQuenue(self,item):
        new = Node(item)

        if self.rear == None:
            self.front = self.rear = new
            return
        self.rear.next = new
        self.rear = new

    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if self.front == None:
            self.rear = None

    def print_queue(self):
        if self.front == None:
            print('lista jest pusta')
        else:
            tmp = self.front
            while tmp:
                print(tmp.data)
                tmp = tmp.next

q = Quene()
q.EnQuenue(10)
q.EnQuenue(20)
q.EnQuenue(56)
q.EnQuenue(40)
q.EnQuenue(17)
q.DeQueue()
print('Queue front ' + str(q.front.data))
print('Queue rear ' + str(q.rear.data))

