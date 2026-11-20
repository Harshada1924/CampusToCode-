try:
    num = int(input("Enter a number: "))

    print(num)

except ValueError:  # hello cannot be converted into an integer using int().
    print("Please enter a valid number!")