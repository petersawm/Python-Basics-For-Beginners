# Functions - reusable blocks of code

# Basic function
def greet():
    print("Hello!")
    print("Welcome to Python")

greet()  # calling the function

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Peter")
greet_person("Sarah")

# Multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)

# Return values
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)

# Multiple return values
def calculate(a, b):
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    return sum_result, diff_result, prod_result

s, d, p = calculate(10, 5)
print(f"Sum: {s}, Diff: {d}, Product: {p}")

# Default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # uses default exponent=2
print(power(5, 3))   # uses exponent=3

# Keyword arguments
def create_profile(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

create_profile(name="John", city="NYC", age=30)

# Variable number of arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))
print(sum_all(5, 10, 15, 20))

# Keyword variable arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Peter", age=30, city="NYC")

# Function with docstring (documentation)
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): Length of rectangle
    width (float): Width of rectangle
    
    Returns:
    float: Area of rectangle
    """
    return length * width

print(calculate_area(5, 3))

# Practical example - calculator
def calculator():
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Choose operation: ")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    
    if choice == "1":
        result = num1 + num2
        print(f"Result: {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"Result: {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"Result: {result}")
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {result}")
        else:
            print("Cannot divide by zero")

# Temperature converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

# Check if number is even
def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False

# Find maximum in list
def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

nums = [5, 2, 9, 1, 7]
print(f"Maximum: {find_max(nums)}")

# Count vowels in string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = "Hello World"
print(f"Vowels in '{text}': {count_vowels(text)}")

# Password validator
def is_valid_password(password):
    if len(password) < 8:
        return False
    has_digit = False
    has_upper = False
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
    return has_digit and has_upper

print(is_valid_password("weak"))        # False
print(is_valid_password("Strong123"))   # True

# Lambda functions (short anonymous functions)
square = lambda x: x ** 2
print(square(5))

add = lambda a, b: a + b
print(add(3, 7))