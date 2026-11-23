#three types of functions
# 1. mathematical functions
import math
a=10
#Square root
print(math.sqrt(a))

#factorial
print(math.factorial(a))

#Power
print(math.pow(a,3))

#Rounds upward
print(math.ceil(4.5))

#Rounds downward
print(math.floor(4.8))


# 2. Random functions

# Importing random module
import random

# Generating a random number between 1 and 10
print(random.randint(1, 10))

# Selecting a random item from a list
names = ["Rahul", "Amit", "Priya", "Sneha"]

print(random.choice(names))


# 3. Trigonometric functions
import math

# Take angle from user
angle = float(input("Enter angle in degrees: "))

# Convert degrees into radians
radian = math.radians(angle)

# Calculate trigonometric values
s = math.sin(radian)
c = math.cos(radian)
t = math.tan(radian)

# Display results
print("Sine:", s)
print("Cosine:", c)
print("Tangent:", t)