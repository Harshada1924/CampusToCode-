try:
    a = 10
    b = 0

    print(a / b)

except ZeroDivisionError:  #Because we want to handle only the error that occurs when dividing by zero.
    print("Cannot divide by zero!")