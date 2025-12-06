# Modules and Imports - using external code

# Import entire module
import math

print(math.pi)
print(math.sqrt(16))
print(math.pow(2, 3))
print(math.ceil(4.3))   # rounds up
print(math.floor(4.7))  # rounds down

# Import specific functions
from math import sqrt, pi
print(sqrt(25))
print(pi)

# Import with alias
import math as m
print(m.sqrt(9))

# Random module
import random

# Random integer between range
num = random.randint(1, 10)
print(f"Random number: {num}")

# Random choice from list
colors = ["red", "blue", "green", "yellow"]
chosen = random.choice(colors)
print(f"Random color: {chosen}")

# Shuffle list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled: {numbers}")

# Random float between 0 and 1
decimal = random.random()
print(f"Random decimal: {decimal}")

# Datetime module
from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")

# Format datetime
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted: {formatted}")

# Date arithmetic
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
print(f"Next week: {next_week.strftime('%Y-%m-%d')}")

# OS module - interact with operating system
import os

# Get current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# List files in directory
files = os.listdir()
print(f"Files: {files}")

# Check if path exists
if os.path.exists("sample.txt"):
    print("File exists")

# Create directory
# os.mkdir("new_folder")

# Get file size
# size = os.path.getsize("sample.txt")
# print(f"File size: {size} bytes")

# Practical example - Number guessing game
def guessing_game():
    import random
    
    number = random.randint(1, 100)
    attempts = 0
    
    print("Guess the number between 1 and 100")
    
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You got it in {attempts} attempts")
                break
        except ValueError:
            print("Please enter a valid number")

# guessing_game()

# Password generator
def generate_password(length=8):
    import random
    import string
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(f"Generated password: {generate_password(12)}")

# Working with JSON
import json

# Dictionary to JSON string
person = {
    "name": "Peter",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(person)
print(f"JSON: {json_string}")

# JSON string to dictionary
json_data = '{"name": "Sarah", "age": 25}'
person_dict = json.loads(json_data)
print(f"Dictionary: {person_dict}")
print(f"Name: {person_dict['name']}")

# Save to JSON file
data = {
    "users": [
        {"name": "Peter", "score": 85},
        {"name": "Sarah", "score": 92}
    ]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

# Read from JSON file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)

# Time module
import time

print("Starting countdown...")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)  # pause for 1 second
print("Done!")

# Measure execution time
start_time = time.time()

# Some operation
total = 0
for i in range(1000000):
    total += i

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.4f} seconds")

# Collections module - useful data structures
from collections import Counter

# Count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(word_count)
print(f"Most common: {word_count.most_common(2)}")

# Count characters
text = "hello world"
char_count = Counter(text)
print(char_count)

# Creating your own module
# Save this in a file called my_math.py:
"""
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(num):
    return num % 2 == 0
"""

# Then import it:
# import my_math
# result = my_math.add(5, 3)
# print(result)