# Dictionaries - store data in key-value pairs

# Creating dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)

# Accessing values
print(person["name"])
print(person["age"])

# Using get method (safer, doesn't error if key missing)
print(person.get("name"))
print(person.get("country"))  # returns None
print(person.get("country", "USA"))  # with default value

# Adding/updating items
person["email"] = "john@email.com"  # add new key
person["age"] = 31  # update existing
print(person)

# Removing items
del person["city"]
print(person)

removed_email = person.pop("email")  # remove and return
print(removed_email)

# Checking if key exists
if "name" in person:
    print("Name exists")

# Getting all keys, values, items
student = {
    "name": "Sarah",
    "grade": 85,
    "subject": "Math"
}

print(student.keys())    # dict_keys(['name', 'grade', 'subject'])
print(student.values())  # dict_values(['Sarah', 85, 'Math'])
print(student.items())   # dict_items([('name', 'Sarah'), ...])

# Looping through dictionary
for key in student:
    print(f"{key}: {student[key]}")

# Better way
for key, value in student.items():
    print(f"{key}: {value}")

# Nested dictionaries
employees = {
    "emp1": {
        "name": "John",
        "salary": 50000
    },
    "emp2": {
        "name": "Jane",
        "salary": 60000
    }
}

print(employees["emp1"]["name"])
print(employees["emp2"]["salary"])

# Dictionary methods
prices = {"apple": 1.50, "banana": 0.75, "orange": 2.00}

# Clear all items
# prices.clear()

# Copy dictionary
new_prices = prices.copy()

# Update with another dictionary
extra_items = {"grape": 3.00, "mango": 2.50}
prices.update(extra_items)
print(prices)

# Practical example - phone book
phonebook = {}

while True:
    print("\n--- Phone Book ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Show all contacts")
    print("6. Exit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        name = input("Name: ")
        number = input("Phone: ")
        phonebook[name] = number
        print(f"Added {name}")
    
    elif choice == "2":
        name = input("Search name: ")
        if name in phonebook:
            print(f"{name}: {phonebook[name]}")
        else:
            print("Contact not found")
    
    elif choice == "3":
        name = input("Name to update: ")
        if name in phonebook:
            number = input("New phone: ")
            phonebook[name] = number
            print(f"Updated {name}")
        else:
            print("Contact not found")
    
    elif choice == "4":
        name = input("Name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(f"Deleted {name}")
        else:
            print("Contact not found")
    
    elif choice == "5":
        print("\nAll contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    
    elif choice == "6":
        break

# Another example - word counter
text = "python is great and python is fun"
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)