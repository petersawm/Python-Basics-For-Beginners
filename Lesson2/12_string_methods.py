# String Methods - powerful text manipulation

# Basic string methods
text = "Hello World"

# Case conversion
print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.title())      # Hello World
print(text.swapcase())   # hELLO wORLD
print(text.capitalize()) # Hello world

# Strip whitespace
message = "   Hello   "
print(message.strip())   # "Hello"
print(message.lstrip())  # "Hello   "
print(message.rstrip())  # "   Hello"

# Find and replace
sentence = "Python is great. Python is fun."
print(sentence.replace("Python", "Programming"))
print(sentence.replace("is", "was", 1))  # replace only first occurrence

# Find substring
text = "Hello World"
print(text.find("World"))    # 6 (index position)
print(text.find("xyz"))      # -1 (not found)
print(text.index("World"))   # 6 (raises error if not found)

# Check if substring exists
if "World" in text:
    print("Found!")

# Count occurrences
sentence = "apple banana apple cherry apple"
print(sentence.count("apple"))  # 3

# Splitting strings
csv_data = "Peter,30,New York"
parts = csv_data.split(",")
print(parts)  # ['Peter', '30', 'New York']

sentence = "Python is awesome"
words = sentence.split()  # splits by whitespace
print(words)

# Split with limit
text = "a-b-c-d-e"
result = text.split("-", 2)  # split only twice
print(result)  # ['a', 'b', 'c-d-e']

# Joining strings
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)

items = ["apple", "banana", "cherry"]
csv = ",".join(items)
print(csv)

# String validation methods
text1 = "Hello123"
text2 = "12345"
text3 = "Hello"

print(text1.isalnum())   # True (alphanumeric)
print(text2.isdigit())   # True (all digits)
print(text3.isalpha())   # True (all letters)
print(text1.isalpha())   # False

email = "user@example.com"
print(email.islower())   # True

# Check start and end
filename = "document.pdf"
print(filename.startswith("doc"))  # True
print(filename.endswith(".pdf"))   # True

url = "https://example.com"
if url.startswith("https://"):
    print("Secure connection")

# String formatting
name = "Peter"
age = 30

# Method 1: f-strings (recommended)
message = f"My name is {name} and I'm {age} years old"
print(message)

# With expressions
price = 19.99
print(f"Total: ${price * 2}")

# Format numbers
num = 3.14159
print(f"Pi: {num:.2f}")  # 2 decimal places

# Method 2: format method
message = "My name is {} and I'm {} years old".format(name, age)
print(message)

# With named placeholders
message = "Name: {n}, Age: {a}".format(n=name, a=age)
print(message)

# Method 3: % formatting (old style)
message = "My name is %s and I'm %d years old" % (name, age)
print(message)

# Padding and alignment
text = "Python"
print(f"{text:>10}")   # right align
print(f"{text:<10}")   # left align
print(f"{text:^10}")   # center align
print(f"{text:*^10}")  # center with padding

# Multiline strings
long_text = """This is a
multiline string
that spans several lines"""
print(long_text)

# Escape characters
print("Line 1\nLine 2")      # newline
print("Tab\tSeparated")      # tab
print("Quote: \"Hello\"")    # quote
print("Path: C:\\Users\\Documents")  # backslash

# Raw strings (ignore escape characters)
path = r"C:\Users\Documents"
print(path)

# Practical examples

# Email validator (simple)
def is_valid_email(email):
    if "@" not in email:
        return False
    if email.count("@") != 1:
        return False
    if "." not in email.split("@")[1]:
        return False
    return True

print(is_valid_email("user@example.com"))  # True
print(is_valid_email("invalid.email"))     # False

# Username validator
def is_valid_username(username):
    if len(username) < 3:
        return False
    if not username.isalnum():
        return False
    return True

print(is_valid_username("user123"))  # True
print(is_valid_username("ab"))       # False

# Clean and format phone number
def format_phone(phone):
    # Remove all non-digit characters
    digits = ''.join(c for c in phone if c.isdigit())
    
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return "Invalid phone number"

print(format_phone("1234567890"))      # (123) 456-7890
print(format_phone("123-456-7890"))    # (123) 456-7890

# Title case for names
def format_name(name):
    return name.strip().title()

print(format_name("PETER SAWM"))      # Peter Sawm
print(format_name("  SARAH SMITH "))  # Sarah Smith

# Extract file extension
def get_file_extension(filename):
    if "." in filename:
        return filename.split(".")[-1]
    return None

print(get_file_extension("document.pdf"))    # pdf
print(get_file_extension("image.png"))       # png

# Word counter
def count_words(text):
    words = text.split()
    return len(words)

text = "Python is a great programming language"
print(f"Word count: {count_words(text)}")

# Reverse string
def reverse_string(text):
    return text[::-1]

print(reverse_string("Hello"))  # olleH

# Check palindrome
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("racecar"))     # True
print(is_palindrome("hello"))       # False
print(is_palindrome("A man a plan a canal Panama"))  # True

# Remove vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in text if char not in vowels)
    return result

print(remove_vowels("Hello World"))  # Hll Wrld

# Censor bad words
def censor_text(text, bad_words):
    for word in bad_words:
        text = text.replace(word, "*" * len(word))
    return text

text = "This is a bad example with bad words"
censored = censor_text(text, ["bad"])
print(censored)