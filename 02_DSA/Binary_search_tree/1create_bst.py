# Operations in BST
#There are four important operations:
#1. Insertion – Add a new node.
#2. Searching – Find a particular node.
#3. Deletion – Remove a node.
#4. Traversal – Visit all nodes.

#create BST
#A node contains three things:
#- Data – Value stored in the node.
#- Left – Address/reference of the left child.
#- Right – Address/reference of the right child.

# Create a node class
class Node:

    def __init__(self, data):

        self.data = data       # Store the value
        self.left = None       # Initially left child is empty
        self.right = None      # Initially right child is empty
node=Node(50)