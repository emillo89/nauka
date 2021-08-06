class Node():
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = Node()

    def add(self,value):
        if self.root.value == None:
            self.root.value = value
        else:
            def add_to_top(value, top):
                if value < top.value:
                    if top.left is None:
                        top.left = Node(value)
                    else:
                        add_to_top(value,top.left)
                if value > top.value:
                    if top.right is None:
                        top.right = Node(value)
                    else:
                        add_to_top(value, top.right)
            add_to_top(value,self.root)

    # inny sposob dodania:
    def add2(self,root, key):
        if root is None:
            return Node(key)
        else:
            if root.value == key:
                return root
            elif root.value < key:
                root.right = self.add2(root.right,key)
            else:
                root.left = self.add2(root.left, key)
        return root

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left

        return current

        # Given a binary search tree and a key, this function
        # delete the key and returns the new root

    def deleteNode(self, root, key):
        # Base Case
        if root is None:
            return root

        # If the key to be deleted
        # is smaller than the root's
        # key then it lies in  left subtree
        if key < root.value:
            root.left = self.deleteNode(root.left, key)

        # If the kye to be delete
        # is greater than the root's key
        # then it lies in right subtree
        elif (key > root.value):
            root.right = self.deleteNode(root.right, key)

        # If key is same as root's key, then this is the node
        # to be deleted
        # wezel z jednym lub z brakiem dzieci
        else:

            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            # wezel z dwoma dziecmi
            temp = self.minValueNode(root.right)

            # Copy the inorder successor's
            # content to this node
            root.value = temp.value

            # Delete the inorder successor
            # usuń nastepce w kolejnosci
            root.right = self.deleteNode(root.right, temp.value)

        return root

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root, '')
        elif traversal_type == 'levelorder':
            return self.levelorder_print(self.root)
        else:
            print('Traversal_type' + str(traversal_type) + ' is not supported')
            return False

    def preorder_print(self, start, traversal):
        '''Root - Left - Right '''
        if start:
            traversal += (str(start.value) + ' - ')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
        # taka powinna być koleność 1 - 2 - 4 - 5 - 3 - 6 - 7 - 8 -

    def inorder_print(self, start, traversal):
        '''Left - Root - Right'''
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + ' - ')
            traversal = self.inorder_print(start.right, traversal)
        return traversal
        # 4 - 2 - 5 - 1 - 6 - 3 - 7 - 8 -

    def postorder_print(self, start, traversal):
        '''Left - Right - Root'''
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + ' - ')
        return traversal
        # 4 - 5 - 2 - 6 - 8 - 7 - 3 - 1 -

drzewo = BST()
drzewo.add(50)
drzewo.add(30)
drzewo.add(20)
drzewo.add(40)
drzewo.add(70)
drzewo.add(60)
drzewo.add(80)

# print(drzewo.print_tree('preorder'))
print(drzewo.print_tree('inorder'))
# print(drzewo.print_tree('postorder'))
drzewo.deleteNode(drzewo.root,20)
print(drzewo.print_tree('inorder'))
drzewo.deleteNode(drzewo.root,30)
print(drzewo.print_tree('inorder'))
drzewo.deleteNode(drzewo.root,50)
print(drzewo.print_tree('inorder'))