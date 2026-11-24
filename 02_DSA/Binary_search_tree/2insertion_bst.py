#insertion logic
#Logic:
#- If the tree is empty, create a new node.
#- If the new value is smaller, go left.
#- If the new value is greater, go right.
#- Repeat until an empty position is found.

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to insert a new value
def insert(root, data):

    # If tree is empty, create a new node
    if root is None:
        return Node(data)

    # If value is smaller, insert on left side
    if data < root.data:
        root.left = insert(root.left, data)

    # If value is greater, insert on right side
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Create an empty tree
root = None

# Insert values
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)
