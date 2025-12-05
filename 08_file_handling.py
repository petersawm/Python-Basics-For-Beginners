# File Handling - reading and writing files

# Writing to a file
file = open("sample.txt", "w")  # "w" = write mode
file.write("Hello, World!\n")
file.write("Python is awesome.\n")
file.close()

# Better way - using 'with' (automatically closes file)
with open("sample.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

# Reading entire file
with open("sample.txt", "r") as file:  # "r" = read mode
    content = file.read()
    print(content)

# Reading line by line
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline

# Reading into a list
with open("sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Appending to file
with open("sample.txt", "a") as file:  # "a" = append mode
    file.write("This is a new line\n")

# Check if file exists
import os

if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File not found")

# Delete file
# os.remove("sample.txt")

# Practical example - save user data
def save_contact(name, phone):
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone}\n")

def read_contacts():
    if not os.path.exists("contacts.txt"):
        print("No contacts found")
        return
    
    with open("contacts.txt", "r") as file:
        for line in file:
            name, phone = line.strip().split(",")
            print(f"{name}: {phone}")

# Save some contacts
save_contact("John", "555-1234")
save_contact("Sarah", "555-5678")

# Read them back
print("All contacts:")
read_contacts()

# Example - note taking app
def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {note}\n")
    print("Note saved!")

def view_notes():
    if not os.path.exists("notes.txt"):
        print("No notes found")
        return
    
    with open("notes.txt", "r") as file:
        notes = file.read()
        if notes:
            print("\n--- Your Notes ---")
            print(notes)
        else:
            print("No notes found")

while True:
    print("\n--- Notes App ---")
    print("1. Add note")
    print("2. View notes")
    print("3. Exit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        break

# Working with CSV-like data
# Save student scores
students = [
    {"name": "John", "score": 85},
    {"name": "Sarah", "score": 92},
    {"name": "Mike", "score": 78}
]

with open("scores.txt", "w") as file:
    file.write("Name,Score\n")
    for student in students:
        file.write(f"{student['name']},{student['score']}\n")

# Read and process scores
with open("scores.txt", "r") as file:
    lines = file.readlines()[1:]  # skip header
    total = 0
    count = 0
    for line in lines:
        name, score = line.strip().split(",")
        score = int(score)
        total += score
        count += 1
        print(f"{name}: {score}")
    
    if count > 0:
        average = total / count
        print(f"\nAverage score: {average:.2f}")

# Exception handling with files
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"Error: {e}")