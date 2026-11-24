
# Three Types of Functions

# 1. Mathematical Functions

import math

a = 10

# Calculates square root
print("Square Root:", math.sqrt(a))

# Calculates factorial
print("Factorial:", math.factorial(a))

# Calculates power
print("Power:", math.pow(a, 3))

# Rounds upward
print("Ceiling:", math.ceil(4.5))

# Rounds downward
print("Floor:", math.floor(4.8))


# 2. Random Functions

# Importing random module
import random

# Generates a random number between 1 and 10
print("Random Number:", random.randint(1, 10))

# Selecting a random item from a list
names = ["Rahul", "Amit", "Priya", "Sneha"]

print("Random Name:", random.choice(names))


# 3. Trigonometric Functions

# Takes angle from user
angle = float(input("Enter angle in degrees: "))

# Converts degrees into radians
radian = math.radians(angle)

# Calculates trigonometric values
s = math.sin(radian)
c = math.cos(radian)
t = math.tan(radian)

# Displays results
print("Sine:", s)
print("Cosine:", c)
print("Tangent:", t)
