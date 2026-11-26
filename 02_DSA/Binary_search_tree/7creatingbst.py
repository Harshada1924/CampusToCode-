#create a node using class

class Node:
    def __init__(self,data):  #constructor ,runs automatically
        self.data=data
        self.right=None
        self.left=None
        
        
root=None  #initially node is empty

#print message if tree is empty
if root is None:
    print("Tree is empty")
else:
    print("Tree is not empty")
    
    
root=Node(50)     #first insertion into an empty tree
root.left=Node(40)
root.right=Node(60)
print("      ",root.data)
print("     ","/  \\")
print("    ",root.left.data," ",root.right.data)


#print message if tree is empty
if root is None:
    print("Tree is empty")
else:
    print("Tree is not empty")