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
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._find_minimum(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)
        return node

    def _find_minimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)    # Traverse the left subtree
            print(node.value, end=" ")            # Print the value of the current node
            self._inorder_recursive(node.right)   # Traverse the right subtree

# Create a binary search tree instance
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
bst.inorder_traversal()  # Output: 20 30 40 50 60 70 80

# Search for a value
result = bst.search(60)
if result:
    print("Found")
else:
    print("Not found")

# Delete a value
bst.delete(20)
bst.inorder_traversal()  # Output: 20 40 50 60 70 80
