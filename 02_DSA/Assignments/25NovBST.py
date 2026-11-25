#Q. 1 E-Commerce Product Search System 
#An e-commerce company maintains product IDs in a BST to enable efficient 
#product searching. 
#Tasks: 
#1. Create a BST using product IDs.  
#Insert the following product IDs:  
#150, 100, 200, 75, 125, 175, 250, 60, 90, 110. 
#2. Display product IDs in ascending order. 
#3. Search for product ID 175 exists. 
#4. Delete product ID 100. 
#5. Display the BST using inorder, preorder, and postorder traversals. 
#6. Find the minimum and maximum product IDs.

#1. Create a BST using product IDs.  
class Node:
    def __init__(self,data):
        self.data=data        # store product id
        self.left=None        #left node is empty
        self.right=None       #right node is empty
        
def insert(root,data):  #to insert product IDs
    if root is None:    #if tree is empty
        return Node(data)
    if data<root.data:              #add to left subtree
        root.left=insert(root.left,data)
    else:                          #add to right subtree
        root.right=insert(root.right,data)
    return root 


#2. Display product IDs in ascending order. 
def inorder(root):            # (LRR)
    if root:
        inorder(root.left)       #visit left subtree
        print(root.data, end=" ")         #print current node value
        inorder(root.right)          # visit the right subtree

def preorder(root):  #(RLR)
    if root:       
        print(root.data, end=" ")  #print the current node value
        preorder(root.left)          # visit the left subtree
        preorder(root.right)           #visit the right subtree

def postorder(root):  #(Left, Right, Root)
    if root:
        postorder(root.left)  #First visit the left subtree
        postorder(root.right)   # Then visit the right subtree
        print(root.data, end=" ")   # print the current node value


#3. Search for product ID 175 exists. 
def search(root, key):
    if root is None:          #value is not found
        return False
    if root.data == key: # If current node value matches the search value
       return True
    if key < root.data:     # If search value is smaller, search in left subtree
        return search(root.left, key)
    else:     # If search value is greater, search in right subtree
        return search(root.right, key)

# Function to delete a product ID
def delete(root, key):
    if root is None:        # If tree is empty, return None
        return root
    
    if key < root.data:      
        root.left = delete(root.left, key)         # Search and delete from left subtree
    elif key > root.data:       # If product ID is greater than current node
        root.right = delete(root.right, key)           # Search and delete from right subtree
    else:       # If product ID is found
        if root.left is None:               #c1 Node has no left child
            return root.right                 # Return right child (or None if there is no child)
        elif root.right is None:          # C2: Node has no right child
            return root.left              # Return left child
        # CASE 3: Node has both left and right children
        temp = root.right                         # Start from the right subtree
        while temp.left:                               # Find the smallest value in the right subtree
            temp = temp.left            # Move towards the left child
        root.data = temp.data          # Replace the deleted node's value with successor value
        root.right = delete(root.right, temp.data)         # Delete the original successor node from right subtree
    return root            # updated node

#Function to find minimum product ID
def find_min(root):
    while root.left:    # Keep moving towards the left child
        root = root.left  
    return root.data      # Return the leftmost node value



# Function to find maximum product ID
def find_max(root):
    while root.right:     # Keep moving towards the right child
        root = root.right         # Move to the right node
    return root.data          # Move to the right node






# the BST is empty
root = None
products = [150, 100, 200, 75, 125, 175, 250, 60, 90, 110] # List of product IDs to insert
for product in products: # Insert each product ID into the BST
    root = insert(root, product)      # Update root after every insertion
print("Product IDs inserted successfully!")


# Display product IDs in ascending order
print("\nProduct IDs in ascending order:")
inorder(root)  # Call inorder function to display sorted values



# Search for product ID 175
print("\n\nSearching for product ID 175:")
if search(root, 175):
    print("Product ID 175 exists.")       # Display message if product is found
else:
    print("Product ID 175 does not exist.")     # Display message if product is not found


#Delete product ID 100
root = delete(root, 100)   # Call delete function and update the root
print("\nProduct ID 100 deleted successfully.")


#Display all three traversals after deletion

# Display Inorder Traversal
print("\nInorder Traversal:")
inorder(root)

# Display Preorder Traversal
print("\nPreorder Traversal:")
preorder(root)

# Display Postorder Traversal
print("\nPostorder Traversal:")
postorder(root)


# Find minimum and maximum product IDs
print("\n\nMinimum Product ID:", find_min(root))
print("Maximum Product ID:", find_max(root))