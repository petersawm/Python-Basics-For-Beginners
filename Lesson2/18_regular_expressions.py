# Regular Expressions (Regex) - Pattern matching in text

import re

# Basic pattern matching
text = "Hello World"
pattern = "World"

# Check if pattern exists
if re.search(pattern, text):
    print("Pattern found!")

# Find all occurrences
text = "The cat sat on the mat"
matches = re.findall("at", text)
print(f"Found 'at': {matches}")  # ['at', 'at', 'at']

# Match at the start of string
text = "Python is great"
if re.match("Python", text):
    print("Starts with Python")

# Common regex patterns

# \d - any digit (0-9)
text = "My number is 12345"
numbers = re.findall(r"\d", text)
print(f"Digits: {numbers}")

# \d+ - one or more digits
numbers = re.findall(r"\d+", text)
print(f"Number groups: {numbers}")

# \w - any word character (letter, digit, underscore)
text = "user_name123"
chars = re.findall(r"\w+", text)
print(f"Word characters: {chars}")

# \s - any whitespace
text = "Hello World"
spaces = re.findall(r"\s", text)
print(f"Spaces: {len(spaces)}")

# . - any character except newline
text = "cat bat rat"
matches = re.findall(r".at", text)
print(f"Matches: {matches}")

# Email validation
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(is_valid_email("user@example.com"))  # True
print(is_valid_email("invalid.email"))     # False

# Phone number extraction
text = "Call me at 555-123-4567 or 555-987-6543"
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phones = re.findall(phone_pattern, text)
print(f"Phone numbers: {phones}")

# URL extraction
text = "Visit https://example.com or http://test.org"
url_pattern = r'https?://[^\s]+'
urls = re.findall(url_pattern, text)
print(f"URLs: {urls}")

# Character classes
# [abc] - matches a, b, or c
# [a-z] - any lowercase letter
# [A-Z] - any uppercase letter
# [0-9] - any digit
# [^abc] - anything except a, b, c

text = "ABC123xyz"
lowercase = re.findall(r'[a-z]+', text)
uppercase = re.findall(r'[A-Z]+', text)
digits = re.findall(r'[0-9]+', text)

print(f"Lowercase: {lowercase}")
print(f"Uppercase: {uppercase}")
print(f"Digits: {digits}")

# Quantifiers
# * - 0 or more
# + - 1 or more
# ? - 0 or 1
# {n} - exactly n times
# {n,} - n or more times
# {n,m} - between n and m times

# Find words with 3-5 characters
text = "The cat sat on a mat"
words = re.findall(r'\b\w{3,5}\b', text)
print(f"3-5 letter words: {words}")

# Grouping and capturing
text = "Peter Sawm, age 30"
pattern = r'(\w+) (\w+), age (\d+)'
match = re.search(pattern, text)

if match:
    first_name = match.group(1)
    last_name = match.group(2)
    age = match.group(3)
    print(f"Name: {first_name} {last_name}, Age: {age}")

# Replace text
text = "Hello World"
new_text = re.sub(r'World', 'Python', text)
print(new_text)  # "Hello Python"

# Replace multiple whitespace with single space
text = "Too    many     spaces"
cleaned = re.sub(r'\s+', ' ', text)
print(cleaned)

# Remove all digits
text = "abc123def456"
no_digits = re.sub(r'\d', '', text)
print(no_digits)  # "abcdef"

# Split string by pattern
text = "apple,banana;cherry:orange"
fruits = re.split(r'[,;:]', text)
print(fruits)

# Password validator
def is_strong_password(password):
    """
    Password must have:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    if len(password) < 8:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'\d', password):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

print(is_strong_password("weak"))           # False
print(is_strong_password("Strong123!"))     # True

# Extract hashtags from text
def extract_hashtags(text):
    pattern = r'#\w+'
    return re.findall(pattern, text)

tweet = "Loving #Python and #Programming! #Code"
hashtags = extract_hashtags(tweet)
print(f"Hashtags: {hashtags}")

# Extract mentions (@username)
def extract_mentions(text):
    pattern = r'@\w+'
    return re.findall(pattern, text)

tweet = "Thanks @user1 and @user2 for the help!"
mentions = extract_mentions(tweet)
print(f"Mentions: {mentions}")

# Validate date format (YYYY-MM-DD)
def is_valid_date(date_string):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, date_string))

print(is_valid_date("2024-12-06"))  # True
print(is_valid_date("12/06/2024"))  # False

# Extract IP addresses
text = "Server IPs: 192.168.1.1, 10.0.0.1, 172.16.0.1"
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ips = re.findall(ip_pattern, text)
print(f"IP addresses: {ips}")

# Credit card masking
def mask_credit_card(number):
    pattern = r'\d{4}-?\d{4}-?\d{4}-?(\d{4})'
    return re.sub(pattern, r'****-****-****-\1', number)

cc = "1234-5678-9012-3456"
masked = mask_credit_card(cc)
print(f"Masked: {masked}")

# Extract prices from text
def extract_prices(text):
    pattern = r'\$\d+\.?\d*'
    return re.findall(pattern, text)

text = "Products cost $19.99, $5.50, and $100"
prices = extract_prices(text)
print(f"Prices: {prices}")

# Clean HTML tags
def remove_html_tags(html):
    pattern = r'<[^>]+>'
    return re.sub(pattern, '', html)

html = "<p>Hello <strong>World</strong></p>"
clean_text = remove_html_tags(html)
print(f"Clean text: {clean_text}")

# Validate username
def is_valid_username(username):
    """
    Username must:
    - Be 3-16 characters
    - Contain only letters, numbers, underscore
    - Start with a letter
    """
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{2,15}$'
    return bool(re.match(pattern, username))

print(is_valid_username("user123"))    # True
print(is_valid_username("1user"))      # False
print(is_valid_username("us"))         # False

# Find duplicate words
def find_duplicate_words(text):
    pattern = r'\b(\w+)\s+\1\b'
    duplicates = re.findall(pattern, text, re.IGNORECASE)
    return duplicates

text = "The the cat sat sat on the mat"
dupes = find_duplicate_words(text)
print(f"Duplicate words: {dupes}")

# Case-insensitive search
text = "Python python PYTHON"
matches = re.findall(r'python', text, re.IGNORECASE)
print(f"Found {len(matches)} matches")

# Multiline matching
text = """Line 1
Line 2
Line 3"""

# ^ matches start of each line with MULTILINE flag
lines = re.findall(r'^Line', text, re.MULTILINE)
print(f"Lines starting with 'Line': {len(lines)}")

# Non-greedy matching
html = "<div>Content 1</div><div>Content 2</div>"

# Greedy (default)
greedy = re.findall(r'<div>.*</div>', html)
print(f"Greedy: {greedy}")

# Non-greedy
non_greedy = re.findall(r'<div>.*?</div>', html)
print(f"Non-greedy: {non_greedy}")

# Lookahead and lookbehind (advanced)
# Positive lookahead (?=...)
text = "Price: $100 USD"
# Find number followed by USD
numbers = re.findall(r'\d+(?= USD)', text)
print(f"Numbers before USD: {numbers}")

# Negative lookahead (?!...)
# Find numbers NOT followed by USD
text = "Price: $100 USD, $50 EUR"
numbers = re.findall(r'\$(\d+)(?! USD)', text)
print(f"Non-USD prices: {numbers}")

# Text sanitization
def sanitize_filename(filename):
    # Remove invalid characters for filenames
    pattern = r'[<>:"/\\|?*]'
    return re.sub(pattern, '_', filename)

filename = "my<file>name?.txt"
safe = sanitize_filename(filename)
print(f"Safe filename: {safe}")

# Word boundaries
text = "cat cats caterpillar"
# \b marks word boundary
matches = re.findall(r'\bcat\b', text)
print(f"Exact 'cat' matches: {matches}")