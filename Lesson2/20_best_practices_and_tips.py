# Python Best Practices and Tips - Writing clean, professional code

# 1. NAMING CONVENTIONS

# Variables and functions - lowercase with underscores
user_name = "Peter"
total_count = 100

def calculate_total_price(items):
    return sum(items)

# Constants - uppercase
MAX_CONNECTIONS = 100
API_KEY = "your-api-key"
DEFAULT_TIMEOUT = 30

# Classes - PascalCase
class UserAccount:
    pass

class DatabaseConnection:
    pass

# Private variables/methods - prefix with underscore
class BankAccount:
    def __init__(self):
        self._balance = 0  # "private" variable
    
    def _validate_amount(self, amount):  # "private" method
        return amount > 0


# 2. CODE STYLE AND FORMATTING (PEP 8)

# Good spacing
def good_function(param1, param2):
    result = param1 + param2
    return result

# Avoid too many nested blocks
# Bad:
def bad_nested(data):
    if data:
        if len(data) > 0:
            if data[0] is not None:
                return data[0]
    return None

# Better - early returns
def good_nested(data):
    if not data:
        return None
    if len(data) == 0:
        return None
    if data[0] is None:
        return None
    return data[0]

# Even better - using guard clauses
def best_nested(data):
    if not data or len(data) == 0 or data[0] is None:
        return None
    return data[0]


# 3. FUNCTION DESIGN

# Good: Single responsibility
def get_user_email(user_id):
    # Only does one thing
    return database.get_user(user_id).email

# Good: Clear function names
def is_valid_email(email):
    return "@" in email and "." in email

def calculate_discount(price, discount_rate):
    return price * discount_rate

# Use default parameters wisely
def create_user(name, age, country="USA", active=True):
    return {
        "name": name,
        "age": age,
        "country": country,
        "active": active
    }


# 4. ERROR HANDLING

# Don't catch all exceptions blindly
# Bad:
def bad_error_handling():
    try:
        risky_operation()
    except:  # Catches everything!
        pass

# Good: Catch specific exceptions
def good_error_handling():
    try:
        risky_operation()
    except ValueError as e:
        print(f"Invalid value: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")

# Use context managers for cleanup
def read_file_safe(filename):
    try:
        with open(filename, 'r') as file:  # Automatically closes
            return file.read()
    except FileNotFoundError:
        return None


# 5. WORKING WITH DATA STRUCTURES

# List comprehensions for simple transformations
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]

# Generator expressions for large datasets
sum_of_squares = sum(x**2 for x in range(1000000))

# Dictionary comprehensions
user_ages = {"Peter": 30, "Sarah": 25, "Mike": 35}
adult_users = {name: age for name, age in user_ages.items() if age >= 18}

# Use dict.get() with defaults
config = {"timeout": 30, "retries": 3}
timeout = config.get("timeout", 10)  # Returns 10 if "timeout" not found

# Unpacking
# Good:
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]


# 6. STRING HANDLING

# Use f-strings for formatting (Python 3.6+)
name = "Peter"
age = 30
message = f"{name} is {age} years old"

# Multi-line strings
long_text = (
    "This is a very long string that "
    "spans multiple lines for better "
    "readability"
)

# Join instead of concatenation in loops
# Bad:
result = ""
for word in ["Hello", "World"]:
    result += word + " "

# Good:
words = ["Hello", "World"]
result = " ".join(words)


# 7. COMPARISON AND CONDITIONALS

# Use 'in' for multiple comparisons
# Good:
if status in ["active", "pending", "new"]:
    process_status(status)

# Use 'is' for None, True, False
if value is None:
    handle_none()

if flag is True:
    do_something()

# Truthiness
# Empty containers are falsy
if not my_list:  # Better than: if len(my_list) == 0:
    print("List is empty")

if my_dict:  # Checks if dict has items
    process_dict(my_dict)


# 8. FUNCTIONS AND CLASSES

# Type hints for clarity (Python 3.5+)
def calculate_area(length: float, width: float) -> float:
    return length * width

def process_names(names: list[str]) -> dict[str, int]:
    return {name: len(name) for name in names}

# Docstrings for documentation
def complex_function(param1, param2):
    """
    Brief description of what the function does.
    
    Args:
        param1 (int): Description of param1
        param2 (str): Description of param2
    
    Returns:
        bool: Description of return value
    
    Raises:
        ValueError: If param1 is negative
    """
    if param1 < 0:
        raise ValueError("param1 must be positive")
    return True


# 9. CLASS DESIGN

# Use __repr__ for debugging
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f"User(name={self.name!r}, email={self.email!r})"
    
    def __str__(self):
        return f"{self.name} ({self.email})"

user = User("Peter", "peter@email.com")
print(repr(user))  # User(name='Peter', email='peter@email.com')
print(str(user))   # Peter (peter@email.com)

# Use properties for computed attributes
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.area)  # Computed property


# 10. ITERATION

# Use enumerate instead of range(len())
# Bad:
for i in range(len(items)):
    print(f"{i}: {items[i]}")

# Good:
for i, item in enumerate(items):
    print(f"{i}: {item}")

# Use zip to iterate multiple lists
names = ["Peter", "Sarah", "Mike"]
ages = [30, 25, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Use itertools for advanced iteration
from itertools import islice, cycle, chain

# Take first 5 items
first_five = list(islice(range(100), 5))


# 11. PERFORMANCE TIPS

# Use sets for membership testing
# Fast:
valid_users = {"Peter", "Sarah", "Mike"}
if user in valid_users:
    process_user(user)

# Use local variables (faster than global)
def calculate():
    local_var = some_global_value  # Cache global in local
    for i in range(1000):
        result = local_var * i

# List comprehension vs map
# Both are fine, use what's readable
numbers = [1, 2, 3, 4, 5]
doubled1 = [x * 2 for x in numbers]
doubled2 = list(map(lambda x: x * 2, numbers))


# 12. FILE OPERATIONS

# Always use context managers
with open("file.txt", "r") as file:
    content = file.read()

# Read large files line by line
with open("large_file.txt", "r") as file:
    for line in file:  # Memory efficient
        process_line(line)


# 13. IMPORTS

# Standard library first, then third-party, then local
import os
import sys

import requests
import pandas

from myproject import mymodule

# Avoid wildcard imports
# Bad: from module import *
# Good: from module import specific_function


# 14. CONSTANTS AND CONFIGURATION

# Use a config file or class
class Config:
    DEBUG = True
    DATABASE_URL = "postgresql://localhost/mydb"
    MAX_CONNECTIONS = 100
    TIMEOUT = 30

# Or use environment variables
import os
API_KEY = os.getenv("API_KEY", "default-key")


# 15. TESTING

# Write testable code
# Bad: Hard to test
def process_data():
    data = fetch_from_api()
    result = complex_calculation(data)
    save_to_database(result)

# Good: Easy to test
def fetch_data():
    return fetch_from_api()

def calculate(data):
    return complex_calculation(data)

def save_result(result):
    save_to_database(result)

def process_data():
    data = fetch_data()
    result = calculate(data)
    save_result(result)


# 16. COMMON PATTERNS

# Singleton pattern
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Factory pattern
def create_shape(shape_type):
    if shape_type == "circle":
        return Circle()
    elif shape_type == "square":
        return Square()


# 17. USEFUL TIPS

# Swap variables
a, b = b, a

# Chain comparisons
if 0 < x < 10:
    print("x is between 0 and 10")

# Dictionary merging (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2

# Ternary operator
status = "active" if is_logged_in else "inactive"

# Multiple assignment
x = y = z = 0

# Walrus operator (Python 3.8+)
if (n := len(data)) > 10:
    print(f"Length is {n}")


# 18. WHAT TO AVOID

# Don't use mutable default arguments
# Bad:
def append_to(element, lst=[]):
    lst.append(element)
    return lst

# Good:
def append_to(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst

# Don't compare boolean values to True/False
# Bad:
if is_active == True:
    pass

# Good:
if is_active:
    pass

# Don't use bare except
# Bad:
try:
    risky()
except:
    pass

# Good:
try:
    risky()
except Exception as e:
    logging.error(f"Error: {e}")


# 19. CODE ORGANIZATION

"""
Project Structure:
project/
    __init__.py
    main.py
    config.py
    models/
        __init__.py
        user.py
        product.py
    utils/
        __init__.py
        helpers.py
    tests/
        test_user.py
        test_product.py
"""


# 20. FINAL TIPS

# Keep functions small (one task)
# Use meaningful variable names
# Comment complex logic, not obvious code
# Write tests
# Use version control (Git)
# Follow PEP 8 style guide
# Read other people's code
# Practice regularly
# Learn from mistakes
# Keep learning!