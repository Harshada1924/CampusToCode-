# Program to handle TypeError

try:
    # Taking an integer
    a = 10

    # Taking a string
    b = "Hello"

    # Adding integer and string
    result = a + b

    # Printing the result
    print(result)

except TypeError:
    # Handling incompatible data types
    print("Cannot add integer and string!")