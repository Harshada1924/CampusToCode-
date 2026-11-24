class Node:
  # Initializes a new BST node with a value and empty left/right children
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


# Finds and returns the node with the smallest value in a given subtree
def find_min(node):
  current = node
  while current.left is not None:  # Keep moving left to reach the minimum
    current = current.left
  return current


# Deletes the node matching 'key' from the BST and returns the updated root
def delete_node(root, key):
  if root is None:  # Base case: empty tree or key not found
    return None

  if key < root.data:  # Key is smaller, search in the left subtree
    root.left = delete_node(root.left, key)
  elif key > root.data:  # Key is larger, search in the right subtree
    root.right = delete_node(root.right, key)
  else:  # Found the node to delete
    # Case 1 (no children) & Case 2 (one child): return the non-None child (or None)
    if root.left is None:
      return root.right
    if root.right is None:
      return root.left

    # Case 3 (two children): find the smallest node in the right subtree (inorder successor)
    successor = find_min(root.right)
    root.data = (
        successor.data
    )  # Copy the successor's value into the current node
    root.right = delete_node(
        root.right, successor.data
    )  # Delete the duplicate successor node

  return root


# Prints all BST node values in ascending sorted order (Left -> Root -> Right)
def inorder(root):
  if root:
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# Example usage
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

root = delete_node(root, 50)
inorder(root)  # Output: 20 30 40 60 70 80
