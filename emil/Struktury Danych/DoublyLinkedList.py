import gc


class Node():
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        # jezeli dodajmey element do istniejacej DLL to ustawiamy nowy element jako prev self.head
        if self.head is not None:
            self.head.prev = new_node
        # nastepnie wskazujemy ze nowy element nie jest juz poprzednikiem tylko glowa, bo zostal dodany
        self.head = new_node

    def insertAfter(self,prev_node, new_data):

        new_node = Node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        #  sprawdzamy czy na pewno wstawiuony przez nas wezel jest tym wezlem
        if new_node.next is not None:
            new_node.next.prev = new_node

    def add_end(self,new_data):

        new_node = Node(new_data)
        last = self.head
        new_node.next = None

        # jezeli linked jest pusta to stworzymy nowa glowe
        if self.head is None:
            self.head.prev = None
            self.head = new_node
            return

        while last.next is not None:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def deleteNode(self,dele):
        # sprawdzamy czy lista istnieje lub czy element do usniecia istnieje
        if self.head is None or dele is None:
            return

    #     jezeli element do usniecia stoi na head
        if self.head == dele:
            self.head = dele.next

    #     zmien nastepny tylko wtedy gdy node do usniecia nie jest ostatni
        if dele.next is not None:
            dele.next.prev = dele.prev
    #     zmien poprzedni tylko wtedy gdy usuwany nie jest  pierwszym node
        if dele.prev is not None:
            dele.prev.next = dele.next

    # zwolnienie pamieci zajmowanej przez del garbage collector
        gc.collect()

    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        # przed zamiana glow sprawdz czy lista nie jest pusta lub czy ma jeden wezel
        if temp is not None:
            self.head = temp.prev


    def print_list(self,node):
        while node is not None:
            print(node.data)
            node = node.next

        # while node is not None:
            print('%d' %(node.data))
            last = node
            node = node.next

        # while last is not None:
        #     print('%d' %(last.data))
        #     last = last.prev


llist = DoublyLinkedList()
llist.push(7)
llist.push(1)
llist.add_end(10)
llist.insertAfter(llist.head.next, 8)
print('----')
llist.print_list(llist.head)
print('----')
llist.deleteNode(llist.head)
llist.deleteNode(llist.head.next)
llist.print_list(llist.head)
