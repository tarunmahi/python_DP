class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if not self.root:
            self.root=Node(value)
        else:
            self.rec_insert(self.root,value)
    def rec_insert(self,node,value):
        if value<node.value:
            if not node.left:
                node.left=Node(value)
            else:
                self.rec_insert(node.left,value)
        else:
            if not node.right:
                node.right=Node(value)
            else:
                self.rec_insert(node.right,value)
                
    def inorder(self):
        self.rec_inorder(self.root)
    def rec_inorder(self,node):
        if node:
            self.rec_inorder(node.left)
            print(node.value,end=" ")
            self.rec_inorder(node.right)
    def search(self,value):
        return self.rec_search(self.root,value)
    def rec_search(self,node,value):
        if node is None or value==node.value:
            return node
        if value<node.value:
            return self.rec_search(node.left,value)
        return self.rec_search(node.right,value)
    def delete(self,value):
        self.root=self.rec_delete(self.root,value)
    def rec_delete(self,node,value):
        if not node:
            return node
        if value<node.value:
            node.left=self.rec_delete(node.left,value)
        elif value>node.value:
            node.right=self.rec_delete(node.right,value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp=self.minimum(node.right)
            node.value=temp.value
            node.right=self.rec_delete(node.right,temp.value)
        return node
    def minimum(self,node):
        temp=node
        while temp.left:
            temp=temp.left
        return temp 

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


# Search for a value
result = bst.search(80)
if result:
    print("Found")
else:
    print("Not found")

# Delete a value
bst.delete(30)
bst.inorder()
