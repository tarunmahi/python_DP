class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.rec_insert(self.root, value)

    def rec_insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.rec_insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.rec_insert(node.right, value)  # Error on this line

    def inorder(self):
        self.rec_inorder(self.root)

    def rec_inorder(self, node):
        if node is not None:
            self.rec_inorder(node.left)
            print(node.value, end=" ")
            self.rec_inorder(node.right)

    def minimum(self):
        node = self.root
        while node.left is not None:
            node = node.left
        print(node.value)

bst = BinarySearchTree()

# Insert values into the tree
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

# Perform inorder traversal to print the elements in sorted order
bst.inorder()  # Output: 20 30 40 50 60 70 80
bst.minimum()  # Output: 20
