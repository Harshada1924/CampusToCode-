# Program to handle ZeroDivisionError

try:
    # Taking input from the user
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # Performing division
    result = a / b

    # Printing the result
    print("Division:", result)

except ZeroDivisionError:
    # Handling division by zero
    print("Cannot divide by zero!")