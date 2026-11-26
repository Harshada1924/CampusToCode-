#hospital patient token managemnet
# scenario : A hospita maintain patient token numbers in a bst
#Each token number is unique , and the hospital wants to retrieve patient records efficiently
#tasks :
#1. insert the following  token numbers into a bst :50 ,30,70,20,40,60,80,10
#2.search for token in sorted token numbers 40
#3. Diaplay all the numbers in sorted order
#4. find the smallest to largest token numbers
#5. delete token number 70  and display the updated bst


# Hospital Patient Token Management using BST


# Step 1: Create a Node
class Node:

    def __init__(self, data):
        self.data = data       # Store token number
        self.left = None       # Reference to left child
        self.right = None      # Reference to right child


# Step 2: Insert a node into BST
def insert(root, data):

    # If tree is empty, create a new node
    if root is None:
        return Node(data)

    # If data is smaller, go to left side
    if data < root.data:
        root.left = insert(root.left, data)

    # If data is greater, go to right side
    elif data > root.data:
        root.right = insert(root.right, data)

    # Return the root node
    return root


# Step 3: Search for a token number
def search(root, key):

    # If node is empty, token is not found
    if root is None:
        return False

    # If token is found
    if root.data == key:
        return True

    # Search in left subtree
    if key < root.data:
        return search(root.left, key)

    # Search in right subtree
    else:
        return search(root.right, key)


# Step 4: Display tokens in sorted order
def inorder(root):

    if root is not None:

        inorder(root.left)       # Visit left subtree

        print(root.data, end=" ") # Print current node

        inorder(root.right)      # Visit right subtree


# Step 5: Find smallest token number
def find_min(root):

    if root is None:
        return None

    # Keep moving towards left
    while root.left is not None:
        root = root.left

    return root.data


# Step 6: Find largest token number
def find_max(root):

    if root is None:
        return None

    # Keep moving towards right
    while root.right is not None:
        root = root.right

    return root.data


# Step 7: Delete a token number
def delete(root, key):

    # If tree is empty or token is not found
    if root is None:
        return None

    # Search on left side
    if key < root.data:
        root.left = delete(root.left, key)

    # Search on right side
    elif key > root.data:
        root.right = delete(root.right, key)

    # Token is found
    else:

        # Case 1: No child
        if root.left is None and root.right is None:
            return None

        # Case 2: Only right child
        elif root.left is None:
            return root.right

        # Case 2: Only left child
        elif root.right is None:
            return root.left

        # Case 3: Two children

        # Find smallest value in right subtree
        successor = find_min_node(root.right)

        # Copy successor value
        root.data = successor.data

        # Delete the duplicate successor node
        root.right = delete(root.right, successor.data)

    return root


# Helper function to find minimum node
def find_min_node(root):

    while root.left is not None:
        root = root.left

    return root


# Function to display tree structure sideways
def display_tree(root, level=0):

    if root is not None:

        display_tree(root.right, level + 1)

        print("    " * level, root.data)

        display_tree(root.left, level + 1)


# MAIN PROGRAM

# Step 1: Insert token numbers
tokens = [50, 30, 70, 20, 40, 60, 80, 10]

root = None

for token in tokens:
    root = insert(root, token)


# Step 2: Display original BST
print("Original BST:")
display_tree(root)


# Step 3: Search token number 40
key = 40

if search(root, key):
    print("\nToken", key, "found!")
else:
    print("\nToken", key, "not found!")


# Step 4: Display tokens in sorted order
print("\nTokens in sorted order:")
inorder(root)
print()


# Step 5: Find smallest and largest tokens
print("\nSmallest token:", find_min(root))
print("Largest token:", find_max(root))


# Step 6: Delete token number 70
root = delete(root, 70)

# Step 7: Display updated BST
print("\nBST after deleting token 70:")
display_tree(root)

print("\nUpdated tokens in sorted order:")
inorder(root)
print()