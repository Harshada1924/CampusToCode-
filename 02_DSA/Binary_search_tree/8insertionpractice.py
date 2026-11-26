# Node class is used to create individual nodes of the BST
class Node:

    # __init__ is a constructor.
    # It automatically runs whenever we create a new Node.
    # self refers to the current node being created.
    # data is the value that we want to store in the node.
    def __init__(self, data):

        self.data = data       # Stores the actual value inside the node.
        self.left = None       # Stores the reference to the left child.
                               # None means there is no left child yet.

        self.right = None      # Stores the reference to the right child.
                               # None means there is no right child yet.


# Function to insert a new value into the BST.
# root represents the current node or starting point of the tree.
# data represents the value that we want to insert.
def insert(root, data):

    # Base condition:
    # If root is None, it means we found an empty position.
    if root is None:

        # Create a new node containing data.
        # Return its reference so that it can be connected to the tree.
        return Node(data)

    # BST rule:
    # If the new value is smaller than the current node's value,
    # it must be inserted into the left subtree.
    if data < root.data:

        # Recursively call insert() for the left child.
        # The returned node reference is connected to root.left.
        root.left = insert(root.left, data)

    # If data is greater than or equal to root.data,
    # insert it into the right subtree.
    else:

        # Recursively call insert() for the right child.
        # The returned node reference is connected to root.right.
        root.right = insert(root.right, data)

    # Return the current root.
    # This keeps the tree connected after insertion.
    return root


# Initially, the tree is empty.
root = None

# Values that we want to insert into the BST.
values = [50, 30, 70, 20, 40]

# Loop through each value in the list.
for value in values:

    # Insert the current value into the BST.
    # Store the returned root reference back in root.
    root = insert(root, value)


# Display the root node's value.
print("Root:", root.data)

# Display the left child's value.
print("Left child:", root.left.data)

# Display the right child's value.
print("Right child:", root.right.data)






