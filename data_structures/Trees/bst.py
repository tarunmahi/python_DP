

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
bst.minimum()
"""
# Search for a value
result = bst.search(60)
if result:
    print("Found")
else:
    print("Not found")

# Delete a value
bst.delete(30)
bst.inorder_traversal()
"""