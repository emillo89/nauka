class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist():
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print('Lista jest pusta')
        else:
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next

    # dodawanie na poczatek
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # dodawanie na koniec listy
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    # dodawanie pomiedzy
    def add_prev(self, prev, new_data):
        if prev is None:
            print('wezel musi znajdowac sie w liscie')
            return
        new_node = Node(new_data)
        new_node.next = prev.next
        prev.next = new_node

    # usuwanie elementu, po key
    def delete(self,key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while(temp) is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None


    # usuwanie elementu po indexie
    def delete_position(self,position):
        temp = self.head
        # jesli linkedlist jest pusty
        if temp is None:
            return

        # jesli trzeba usunac glowe
        if position == 0:
            self.head = temp.next
            temp = None
            return
        # znajdz poprzedni wezel wezla do usuniecia
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        # wezel stojacy po indexie ktory chcemy usunac
        dalej = temp.next.next

        # odlaczenie listy od wezla
        temp.next = None
        temp.next = dalej


    # przeniesienie ostatniego elementu na poczatek
    def moveToFront(self):
        tmp = self.head
        # przedostatni wezel
        sec_last = None

        # sprawdzamy czy wezel jest pusty lub czy sklada sie z jednego elementu
        if not tmp or not tmp.next:
            return

        # zapetlenie az otrzymamy przedostatni i ostatni element
        while tmp and tmp.next:
            sec_last = tmp
            tmp = tmp.next

        # ostatni wezel jest pusty
        sec_last.next = None

        # ostatni wezel jest pierwszym wezlem
        tmp.next = self.head
        self.head = tmp

    # usuniecie duplikatow posortowanej linkedlisty
    def remove_duplication(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head

    # usuniecie duplikatow nieposortowanej linkedlisty
    def remove_duplication_not_sorted(self,head):
        # jesli lista jest pusta lub posiada tylko jeden element
        if self.head is None or self.head.next is None:
            return head

        # hash do przechowywania elementow
        hash = set()

        current = head
        hash.add(self.head.data)

        while current.next is not None:
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
        return head

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def swap_wymiana(self,x,y):
        # nic nie rob jesli element ktory chcesz wymienic jest taki sam jak element na ktory chcesz wymienic
        if x == y:
            return
        # znajdujemy X prevX i currX
        prevX = None
        currX = self.head

        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head

        while currY != None and currY.data != y:
            prevX = currY
            currX = currY.next

        # jesli nie ma x lub y nic nie rob:
        if currX == None or currY == None:
            return
        # jesli x nie jest glowa listy
        if prevX != None:
            prevX.next = currY
        #     w innym wypadku stworz glowe Y
        else:
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp



















llist = linkedlist()
llist.push(8)
llist.push(4)
llist.push(4)
llist.push(4)
llist.push(1)

llist.add_end(11)
llist.add_prev(llist.head.next,8)
llist.print_list()
print('----')
llist.delete(4)
llist.print_list()
print('----')
llist.delete_position(2)
llist.print_list()
print('----')
llist.moveToFront()
llist.print_list()
print('----')
llist.remove_duplication()
llist.print_list()
print('----')
llist.remove_duplication_not_sorted(llist.head)
llist.print_list()
print('--zz--')
llist.reverse()
llist.print_list()
print('---zz-')
# llist.swap_wymiana()
# llist.print_list(0,2)