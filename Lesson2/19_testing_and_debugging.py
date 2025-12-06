# Testing and Debugging - Writing reliable code

# Basic print debugging
def calculate_total(prices):
    print(f"DEBUG: Input prices: {prices}")
    total = sum(prices)
    print(f"DEBUG: Total calculated: {total}")
    return total

prices = [10, 20, 30]
result = calculate_total(prices)

# Using assert for simple tests
def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

# This works
result = divide(10, 2)
print(result)

# This raises AssertionError
# result = divide(10, 0)

# Unit testing with unittest
import unittest

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class TestMathFunctions(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)
    
    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)
    
    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
    
    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

# Run tests
# if __name__ == "__main__":
#     unittest.main()

# Testing with edge cases
class Calculator:
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Runs before each test
        self.calc = Calculator()
    
    def test_divide_normal(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)
    
    def test_divide_by_zero(self):
        # Test that exception is raised
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_divide_negative(self):
        result = self.calc.divide(-10, 2)
        self.assertEqual(result, -5)

# Using doctest - tests in docstrings
def factorial(n):
    """
    Calculate factorial of n.
    
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Run doctests
# import doctest
# doctest.testmod()

# Debugging with breakpoint()
def buggy_function(x, y):
    result = x + y
    # breakpoint()  # Execution pauses here for debugging
    return result * 2

# Try-except for debugging
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")
        return None
    except TypeError as e:
        print(f"Type error: {e}")
        return None

result = safe_divide(10, 0)
print(f"Result: {result}")

# Logging for better debugging
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_data(data):
    logging.debug(f"Processing data: {data}")
    
    if not data:
        logging.warning("Empty data received")
        return None
    
    try:
        result = sum(data) / len(data)
        logging.info(f"Calculated average: {result}")
        return result
    except TypeError:
        logging.error("Invalid data type")
        return None

# Different log levels
logging.debug("This is debug info")
logging.info("This is general info")
logging.warning("This is a warning")
logging.error("This is an error")
logging.critical("This is critical")

# Testing string functions
def reverse_string(s):
    return s[::-1]

class TestStringFunctions(unittest.TestCase):
    def test_reverse_simple(self):
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_reverse_empty(self):
        self.assertEqual(reverse_string(""), "")
    
    def test_reverse_single_char(self):
        self.assertEqual(reverse_string("a"), "a")

# Testing with mock data
class UserManager:
    def get_user_age(self, user_id):
        # Pretend this calls a database
        users = {1: 25, 2: 30, 3: 35}
        return users.get(user_id)
    
    def is_adult(self, user_id):
        age = self.get_user_age(user_id)
        if age is None:
            return False
        return age >= 18

class TestUserManager(unittest.TestCase):
    def test_is_adult_true(self):
        manager = UserManager()
        self.assertTrue(manager.is_adult(1))
    
    def test_is_adult_nonexistent(self):
        manager = UserManager()
        self.assertFalse(manager.is_adult(999))

# Debugging tips
def debugging_example():
    """
    Common debugging techniques:
    1. Print statements
    2. Logging
    3. breakpoint()
    4. Using debugger
    5. Unit tests
    6. Assert statements
    """
    
    # Check variable values
    x = 10
    y = 20
    print(f"x={x}, y={y}")
    
    # Check types
    print(f"Type of x: {type(x)}")
    
    # Check if variable exists
    if 'z' in locals():
        print("z exists")
    else:
        print("z does not exist")
    
    # Check object attributes
    class Person:
        def __init__(self, name):
            self.name = name
    
    person = Person("Peter")
    print(f"Person attributes: {dir(person)}")

# Common bugs and fixes

# Bug 1: Mutable default arguments
def append_to_list(item, lst=[]):  # BAD!
    lst.append(item)
    return lst

# Better:
def append_to_list_fixed(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# Bug 2: Variable scope
total = 0

def add_to_total(value):
    global total  # Need this to modify global variable
    total += value

add_to_total(10)
print(total)

# Bug 3: Integer division in Python 2 style
# In Python 3, use / for float division, // for integer division
result1 = 5 / 2   # 2.5
result2 = 5 // 2  # 2

# Bug 4: Comparing with None
value = None
if value is None:  # Correct
    print("Value is None")

# Don't use:
# if value == None:

# Performance profiling
import time

def slow_function():
    start = time.time()
    
    # Simulate slow operation
    total = 0
    for i in range(1000000):
        total += i
    
    end = time.time()
    print(f"Time taken: {end - start:.4f} seconds")
    return total

# slow_function()

# Memory debugging
import sys

def check_object_size():
    numbers = list(range(1000))
    size = sys.getsizeof(numbers)
    print(f"List size: {size} bytes")

# Exception chaining
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError as e:
        raise ValueError(f"Cannot process {filename}") from e
    except ValueError as e:
        raise RuntimeError("Invalid data format") from e

# Context managers for cleanup
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()

# Usage:
# with FileHandler("data.txt") as file:
#     content = file.read()

# Validation helpers
def validate_positive_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if value <= 0:
        raise ValueError("Value must be positive")
    return True

# Testing edge cases
def test_edge_cases():
    test_values = [
        0,           # Zero
        -1,          # Negative
        None,        # None
        "",          # Empty string
        [],          # Empty list
        float('inf'),# Infinity
        float('nan') # Not a number
    ]
    
    for value in test_values:
        print(f"Testing with: {value}")
        # Test your function here

# Best practices for testing
"""
1. Test normal cases
2. Test edge cases (0, empty, None)
3. Test error cases
4. Test boundary values
5. Use descriptive test names
6. Keep tests independent
7. Test one thing per test
8. Use setUp and tearDown
9. Mock external dependencies
10. Aim for high code coverage
"""