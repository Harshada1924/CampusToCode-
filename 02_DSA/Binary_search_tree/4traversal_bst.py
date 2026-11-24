#Traversal means visiting every node of the tree.

#There are three important types of depth-first traversal:
#Traversal	Order
#Inorder	Left → Root → Right
#Preorder	Root → Left → Right
#Postorder	Left → Right → Root

#A. Inorder Traversal
#Order: Left → Root → Right
class Node:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def inorder(root):
  if root:
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)



#B. Preorder Traversal
#Order: Root → Left → Right
def preorder(root):

    if root:
        print(root.data, end=" ") # Print root
        preorder(root.left)       # Visit left side
        preorder(root.right)      # Visit right side



#C. Postorder Traversal
#Order: Left → Right → Root
def postorder(root):

    if root:
        postorder(root.left)       # Visit left side
        postorder(root.right)      # Visit right side
        print(root.data, end=" ")  # Print root


# Build the tree and assign it to root
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)
preorder(root)
postorder(root)

