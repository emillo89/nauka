'''
Drzewo binarne - jest struktura danych, czyli sposobem organizowania danych w pamieci komputera.
Drzewo sklada sie z wierzcholkow, ktore laczone sa poprzez krawedzie(galezie).
https://www.youtube.com/watch?v=nYWhh-akie0&t=10s

Zależność w drzewie binarnym:
każde lewe dziecko jest mniejsza od rodzica, a każde dziecko po prawej jest wieksze od rodzica -
ten porzadek nazywamy BST -binary search tree(binarne drzewo poszukiwan)

przejscia po drzewie binarnym:
-pre-order wzdluzne VLR - korzen. lewy, prawy 3-2-1-8-7-99
-in-order poprzeczny LVR - lewy korzen prawy 1-2-3-7-8-99
--order - wsteczne LRV - lewy prawy korzen - 1-2-7-99-8-3
'''

class Queue():
    def __init__(self):
        self.items = []

    def enque(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_Empty():
            return self.items.pop()

    def is_Empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_Empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)



class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binarytree():
    def __init__(self,root):
        self.root = Node(root)

    def print_tree(self,traversal_type):
        if traversal_type ==  'preorder':
            return self.preorder_print(tree.root,'')
        elif traversal_type == 'inorder':
            return self.inorder_print(tree.root,'')
        elif traversal_type == 'postorder':
            return self.postorder_print(tree.root, '')
        elif traversal_type == 'levelorder':
            return self.levelorder_print(tree.root)
        else:
            print('Traversal_type' + str(traversal_type) + ' is not supported')
            return False



    def preorder_print(self,start,traversal):
        '''Root - Left - Right '''
        if start:
            traversal += (str(start.value) + ' - ')
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
        # taka powinna być koleność 1 - 2 - 4 - 5 - 3 - 6 - 7 - 8 -

    def inorder_print(self, start, traversal):
        '''Left - Root - Right'''
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal += (str(start.value) + ' - ')
            traversal = self.inorder_print(start.right, traversal)
        return traversal
        # 4 - 2 - 5 - 1 - 6 - 3 - 7 - 8 -

    def postorder_print(self,start, traversal):
        '''Left - Right - Root'''
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + ' - ')
        return traversal
        # 4 - 5 - 2 - 6 - 8 - 7 - 3 - 1 -

    def levelorder_print(self,start):
        if start is None:
            return

        queue = Queue()
        queue.enque(start)

        traversal = ''

        while len(queue) > 0:
            traversal += str(queue.peek()) + ' - '
            node = queue.dequeue()

            if node.left:
                queue.enque(node.left)

            if node.right:
                queue.enque(node.right)
        return traversal


    def insert(self, temp, key):
        if not temp:
            self.root = Node(key)
            return

        q = []
        q.append(temp)

        while len(q):
            var = q[0]
            q.pop(0)

            if not var.left:
                var.left = Node(key)
                break
            else:
                q.append(var.left)

            if not var.right:
                var.right = Node(key)
                break
            else:
                q.append(var.right)


    # function to delete the given deepest node (d_node) in binary tree
    def deleteDeepest(self, root, d_node):
        q = []
        q.append(root)

        while len(q):
            tmp = q.pop(0)


            if tmp is d_node:
                tmp = None
                return
            if tmp.right:
                if tmp.right is d_node:
                    tmp.right = None
                    return
                else:
                    q.append(tmp.right)

            if tmp.left:
                if tmp.left is d_node:
                    tmp.left = None
                    return
                else:
                    q.append(tmp.left)


    def delection(self, root, key):
        if root == None:
            return None
        if root.left == None and root.right == None:
            if root.value == key:
                return None
            else:
                return root

        key_node = None

        q = []
        q.append(root)

        while len(q):
            temp = q.pop(0)

            if temp.value == key:
                key_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

        if key_node:
            x = temp.value
            self.deleteDeepest(root, temp)
            key_node.value = x
        return root


tree = Binarytree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

tree.insert(tree.root,100)
print('---')

print('Preorder: ',end = '')
print(tree.print_tree('preorder'))
print('---')
print('Inorder: ',end = '')
print(tree.print_tree('inorder'))
print('---')
print('Postorder : ',end = '')
print(tree.print_tree('postorder'))
print('----')
print('Levelorder : ',end = '')
print(tree.print_tree('levelorder'))
print('----')
print('Delection : ',end = '')
tree.delection(tree.root, 100)
print(tree.print_tree('preorder'))
print('---')

li = []

li.append(5)
li.append(510)
print(li)