#Searching means finding whether a particular value exists in the tree.

#Suppose we want to search for 40.
#Steps:
#1. Start from root 50.
#2. 40 is smaller than 50, so go left.
#3. Reach 30.
#4. 40 is greater than 30, so go right.
#5. Reach 40. Value found!
# Function to search a value
# Create a Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to insert values
def insert(root, data):

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Function to search a value
def search(root, key):

    # If tree is empty
    if root is None:
        return False

    # If value is found
    if root.data == key:
        return True

    # Search on left side
    if key < root.data:
        return search(root.left, key)

    # Search on right side
    else:
        return search(root.right, key)


# Create an empty BST
root = None

# Insert values into BST
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)


# Search for 40
if search(root, 40):
    print("Value found")
else:
    print("Value not found")