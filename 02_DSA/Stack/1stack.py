# Create an empty list to act as the stack (end of list = top of stack)
stack = []


# Push (add) an element onto the top of the stack
def push(item):
  stack.append(item)
  print(f"Pushed {item} -> Stack: {stack}")


# Pop (remove and return) the top element from the stack
def pop():
  if is_empty():  # Prevent error when popping from an empty stack
    print("Stack is empty! Cannot pop.")
    return None
  item = stack.pop()
  print(f"Popped {item} -> Stack: {stack}")
  return item


# Peek (view) the top element without removing it
def peek():
  if is_empty():
    print("Stack is empty! Nothing on top.")
    return None
  return stack[-1]


# Check whether the stack has no elements
def is_empty():
  return len(stack) == 0


# Example usage
push(10)
push(20)
push(30)
print("Top element:", peek())  # Output: 30
pop()  # Removes 30
pop()  # Removes 20
print("Is empty?", is_empty())  # Output: False
