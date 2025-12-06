# List Comprehensions - elegant way to create lists

# Traditional way
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)

# List comprehension way
squares = [i ** 2 for i in range(10)]
print(squares)

# Basic syntax: [expression for item in iterable]

# Create list of even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

# Create list of odd numbers
odds = [x for x in range(20) if x % 2 != 0]
print(odds)

# Double each number
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(doubled)

# Convert to uppercase
names = ["Peter", "Sarah", "Mike"]
upper_names = [name.upper() for name in names]
print(upper_names)

# Get lengths of words
words = ["python", "is", "awesome"]
lengths = [len(word) for word in words]
print(lengths)

# Filter with condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater_than_five = [x for x in numbers if x > 5]
print(greater_than_five)

# Multiple conditions
numbers = range(1, 21)
result = [x for x in numbers if x % 2 == 0 if x % 3 == 0]
print(result)  # divisible by both 2 and 3

# If-else in list comprehension
numbers = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(labels)

# Nested loops
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)

# Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for sublist in nested for num in sublist]
print(flat)

# String manipulation
sentence = "Hello World"
chars = [char for char in sentence if char != ' ']
print(chars)

# Get only vowels
text = "Python Programming"
vowels = [char for char in text.lower() if char in 'aeiou']
print(vowels)

# Working with multiple lists
list1 = [1, 2, 3]
list2 = [10, 20, 30]
combined = [x + y for x, y in zip(list1, list2)]
print(combined)

# Cartesian product
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
combinations = [(color, size) for color in colors for size in sizes]
print(combinations)

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print(swapped)

# Filter dictionary
scores = {"Peter": 85, "Sarah": 92, "Mike": 78, "Lisa": 95}
high_scores = {name: score for name, score in scores.items() if score >= 90}
print(high_scores)

# Set comprehension
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_squares = {x**2 for x in numbers}
print(unique_squares)

# Practical examples

# Get all .txt files
files = ["doc.txt", "image.png", "data.txt", "photo.jpg"]
txt_files = [f for f in files if f.endswith(".txt")]
print(txt_files)

# Extract numbers from mixed list
mixed = [1, "hello", 3.14, "world", 42, "python"]
numbers_only = [x for x in mixed if isinstance(x, (int, float))]
print(numbers_only)

# Clean data
data = ["  Peter  ", "Sarah", "  Mike  ", "Lisa"]
cleaned = [name.strip() for name in data]
print(cleaned)

# Generate multiplication table
table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
for row in table:
    print(row)

# Parse CSV-like data
csv_data = "Peter,30,NYC\nSarah,25,LA\nMike,35,Chicago"
lines = csv_data.split("\n")
parsed = [line.split(",") for line in lines]
print(parsed)

# Create dictionary from lists
names = ["Peter", "Sarah", "Mike"]
ages = [30, 25, 35]
people = {name: age for name, age in zip(names, ages)}
print(people)

# Filter and transform
prices = [10.50, 20.00, 15.75, 30.00, 25.50]
discounted = [price * 0.9 for price in prices if price > 20]
print(discounted)

# Word frequency (simple)
text = "python is great python is fun python is easy"
words = text.split()
word_freq = {word: words.count(word) for word in set(words)}
print(word_freq)

# Generate password characters
import random
import string
password_chars = [random.choice(string.ascii_letters + string.digits) for _ in range(8)]
password = ''.join(password_chars)
print(f"Password: {password}")

# Fizz Buzz using comprehension
fizzbuzz = ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 31)]
print(fizzbuzz)

# Extract email domains
emails = ["user@gmail.com", "admin@yahoo.com", "info@company.com"]
domains = [email.split("@")[1] for email in emails]
print(domains)

# Get initials from names
full_names = ["Peter Sawm", "Sarah Smith", "Peter Sawm"]
initials = [''.join([word[0] for word in name.split()]) for name in full_names]
print(initials)

# Convert Celsius to Fahrenheit
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = [(temp * 9/5) + 32 for temp in celsius_temps]
print(fahrenheit_temps)

# Remove duplicates while preserving order
numbers = [1, 2, 2, 3, 4, 4, 5]
seen = set()
unique = [x for x in numbers if not (x in seen or seen.add(x))]
print(unique)

# Grade calculator
scores = [85, 92, 78, 95, 88, 76]
grades = ["A" if s >= 90 else "B" if s >= 80 else "C" if s >= 70 else "D" if s >= 60 else "F" for s in scores]
print(grades)

# Performance note: List comprehensions are faster than loops
import time

# Using loop
start = time.time()
result1 = []
for i in range(1000000):
    result1.append(i ** 2)
loop_time = time.time() - start

# Using comprehension
start = time.time()
result2 = [i ** 2 for i in range(1000000)]
comp_time = time.time() - start

print(f"Loop time: {loop_time:.4f}s")
print(f"Comprehension time: {comp_time:.4f}s")
print(f"Comprehension is {loop_time/comp_time:.2f}x faster")