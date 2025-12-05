# Error Handling - dealing with errors gracefully

# Without error handling - program crashes
# num = int("abc")  # ValueError

# With try-except
try:
    num = int("abc")
except ValueError:
    print("That's not a valid number!")

# Catching specific errors
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Index out of range!")

# Multiple except blocks
def divide_numbers():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Try-except-else-finally
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    # Runs if no error occurred
    print("File read successfully")
    print(content)
finally:
    # Always runs, even if error occurred
    print("Closing operations...")
    # file.close()

# Practical example - safe user input
def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

age = get_integer("Enter your age: ")
print(f"Your age is {age}")

# Calculator with error handling
def safe_calculator():
    while True:
        try:
            print("\n--- Calculator ---")
            num1 = float(input("First number: "))
            operator = input("Operator (+, -, *, /): ")
            num2 = float(input("Second number: "))
            
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = num1 / num2
            else:
                raise ValueError("Invalid operator")
            
            print(f"Result: {result}")
            
            again = input("Calculate again? (y/n): ")
            if again.lower() != "y":
                break
                
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Raising custom errors
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

try:
    check_age(-5)
except ValueError as e:
    print(e)

# File handling with error checking
def read_file_safe(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read {filename}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

content = read_file_safe("myfile.txt")
if content:
    print(content)

# List access with error handling
def safe_list_access(lst, index):
    try:
        return lst[index]
    except IndexError:
        print(f"Index {index} is out of range")
        return None

numbers = [1, 2, 3, 4, 5]
value = safe_list_access(numbers, 10)
print(f"Value: {value}")

# Dictionary access with error handling
def safe_dict_access(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        print(f"Key '{key}' not found")
        return None

person = {"name": "Peter", "age": 30}
email = safe_dict_access(person, "email")

# Validating user input
def get_positive_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num <= 0:
                raise ValueError("Number must be positive")
            return num
        except ValueError as e:
            print(f"Invalid input: {e}")

# price = get_positive_number("Enter price: ")

# Custom exception class
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Email must contain @")
    if "." not in email:
        raise InvalidEmailError("Email must contain .")
    return True

try:
    validate_email("invalid_email")
except InvalidEmailError as e:
    print(f"Email error: {e}")

# Nested try-except
try:
    data = input("Enter a number: ")
    try:
        num = int(data)
        result = 100 / num
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero")
except ValueError:
    print("Invalid number format")