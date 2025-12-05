# Lists - storing multiple items in one variable

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

print(fruits)

# Accessing items (indexing starts at 0)
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # cherry (last item)
print(fruits[-2])  # banana (second from end)

# Changing items
fruits[1] = "blueberry"
print(fruits)

# List length
print(len(fruits))

# Adding items
fruits.append("orange")  # add to end
print(fruits)

fruits.insert(1, "mango")  # insert at position
print(fruits)

# Removing items
fruits.remove("cherry")  # remove by value
print(fruits)

last_fruit = fruits.pop()  # remove and return last item
print(last_fruit)
print(fruits)

fruits.pop(0)  # remove item at index 0
print(fruits)

# Checking if item exists
if "apple" in fruits:
    print("We have apples")
else:
    print("No apples")

# Looping through lists
print("\nAll fruits:")
for fruit in fruits:
    print(f"- {fruit}")

# Loop with index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Better way with enumerate
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# List slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])    # [2, 3, 4]
print(numbers[:4])     # [0, 1, 2, 3]
print(numbers[5:])     # [5, 6, 7, 8, 9]
print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd item)
print(numbers[::-1])   # reverse the list

# Sorting
scores = [85, 92, 78, 95, 88]
scores.sort()  # sorts in place
print(scores)

scores.sort(reverse=True)  # descending order
print(scores)

# Sorted function (creates new list)
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(original)      # unchanged
print(sorted_list)   # sorted

# List methods
numbers = [1, 2, 3, 2, 4, 2, 5]
print(numbers.count(2))    # count occurrences
print(numbers.index(4))    # find index of value

numbers.reverse()          # reverse in place
print(numbers)

# Joining lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)

list1.extend(list2)  # add list2 items to list1
print(list1)

# Copying lists
original = [1, 2, 3]
copy = original.copy()  # or original[:]
copy.append(4)
print(original)  # [1, 2, 3]
print(copy)      # [1, 2, 3, 4]

# List comprehension (advanced but useful)
squares = [x**2 for x in range(10)]
print(squares)

even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)

# Practical example - shopping list
shopping_list = []

while True:
    print("\n--- Shopping List ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Done")
    
    choice = input("Choose: ")
    
    if choice == "1":
        item = input("Item to add: ")
        shopping_list.append(item)
        print(f"Added {item}")
    elif choice == "2":
        item = input("Item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed {item}")
        else:
            print("Item not found")
    elif choice == "3":
        print("\nYour shopping list:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    elif choice == "4":
        break