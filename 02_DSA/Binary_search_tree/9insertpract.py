class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        
        
def insert(root,data):    
    if root is None:
        return node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
        
    return root
    
    
      
root = None
values=[50,60,70,80,20]
for value in values:
    root=insert(root,value)
    
print(root.data)
print(root.left.data)
print(root.right.data)
