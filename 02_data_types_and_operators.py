# Different data types in Python

# Numbers
integer_num = 42
float_num = 3.14
print(type(integer_num))  # <class 'int'>
print(type(float_num))    # <class 'float'>

# Strings
message = "Python is fun"
quote = 'Single quotes work too'
multi_line = """This is a
multi-line
string"""

# Boolean
is_raining = False
has_umbrella = True

# Basic arithmetic operators
a = 10
b = 3
print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Power:", a ** b)          # 1000

# Comparison operators
x = 5
y = 8
print(x == y)  # False (equal to)
print(x != y)  # True (not equal to)
print(x < y)   # True (less than)
print(x > y)   # False (greater than)
print(x <= 5)  # True (less than or equal)
print(x >= 5)  # True (greater than or equal)

# Logical operators
age = 20
has_license = True
print(age >= 18 and has_license)  # True
print(age < 18 or has_license)    # True
print(not has_license)             # False

# String operations
text = "Python"
print(len(text))          # 6 (length)
print(text.upper())       # PYTHON
print(text.lower())       # python
print(text[0])            # P (first character)
print(text[-1])           # n (last character)
print(text[0:3])          # Pyt (slicing)
print("Py" in text)       # True (check if substring exists)

# Type conversion
num_str = "123"
num_int = int(num_str)
print(type(num_int))

price = 19.99
price_int = int(price)
print(price_int)  # 19

number = 42
number_str = str(number)
print(type(number_str))