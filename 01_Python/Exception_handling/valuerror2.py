# Program to handle ValueError

try:
    # Taking a number from the user
    num = int(input("Enter a number: "))

    # Printing the number
    print("Number:", num)

except ValueError:
    # Executes when the input cannot be converted into an integer
    print("Please enter a valid number!")