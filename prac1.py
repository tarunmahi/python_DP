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
                node.left = Node(value)  # Create a new node on the left if it is empty
            else:
                self._insert_recursive(node.left, value)  # Recursively insert into the left subtree
        else:
            if node.right is None:
                node.right = Node(value)  # Create a new node on the right if it is empty
            else:
                self._insert_recursive(node.right, value)  # Recursively insert into the right subtree

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node  # Return the node if it is found or reached the end of the tree
        if value < node.value:
            return self._search_recursive(node.left, value)  # Recursively search in the left subtree
        return self._search_recursive(node.right, value)  # Recursively search in the right subtree

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node  # Return None if the node is not found
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)  # Recursively delete in the left subtree
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)  # Recursively delete in the right subtree
        else:
            if node.left is None:
                return node.right  # Replace the node with its right subtree if left subtree is empty
            elif node.right is None:
                return node.left  # Replace the node with its left subtree if right subtree is empty
            temp = self._find_minimum(node.right)  # Find the minimum value in the right subtree
            node.value = temp.value  # Replace the value of the node with the minimum value
            node.right = self._delete_recursive(node.right, temp.value)  # Delete the minimum value from the right subtree
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
            self._inorder_recursive(node.left)  # Traverse the left subtree
            print(node.value, end=" ")  # Print the value of the current node
            self._inorder_recursive(node.right)  # Traverse the right subtree

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
bst.inorder_traversal()  # Output: 20 30 
