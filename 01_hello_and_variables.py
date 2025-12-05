# First Python Program
print("Hello, World!")
print("Welcome to Python programming")

# Variables - think of them as boxes that store information
name = "Peter"
age = 28
height = 5.8
is_student = True

print(name)
print(age)

# You can change variable values
age = 26
print("New age:", age)

# Multiple variables at once
x, y, z = 10, 20, 30
print(x, y, z)

# Basic math with variables
num1 = 15
num2 = 7
total = num1 + num2
print("Total:", total)

# String operations
first_name = "Sarah"
last_name = "Miller"
full_name = first_name + " " + last_name
print(full_name)

# Getting input from user
user_name = input("What's your name? ")
print("Nice to meet you,", user_name)

# Converting input to number
user_age = input("How old are you? ")
user_age = int(user_age)  # Convert string to integer
print("Next year you'll be", user_age + 1)