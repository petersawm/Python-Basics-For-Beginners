# Loops - doing things repeatedly

# While loop - repeats while condition is true
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1  # same as count = count + 1

# Be careful of infinite loops!
# while True:
#     print("This will run forever")

# While loop with user input
password = ""
while password != "python123":
    password = input("Enter password: ")
    if password != "python123":
        print("Wrong password, try again")
print("Access granted!")

# For loop - iterate over a sequence
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Range with start and end
for num in range(1, 6):  # 1, 2, 3, 4, 5
    print(num)

# Range with step
for num in range(0, 11, 2):  # 0, 2, 4, 6, 8, 10
    print(num)

# Looping through strings
name = "Python"
for letter in name:
    print(letter)

# Break - exits the loop
for i in range(10):
    if i == 5:
        break
    print(i)  # prints 0 to 4

# Continue - skips current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # prints 0, 1, 3, 4 (skips 2)

# Practical example - multiplication table
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Countdown timer
print("Countdown:")
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")

# Sum of numbers
total = 0
for num in range(1, 101):
    total += num
print(f"Sum of 1 to 100: {total}")

# Finding even numbers
print("Even numbers from 1 to 20:")
for num in range(1, 21):
    if num % 2 == 0:
        print(num, end=" ")
print()  # new line

# Nested loops - loops inside loops
print("\nMultiplication table:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}x{j}={i*j}", end="\t")
    print()  # new line after each row

# Pattern printing
rows = 5
for i in range(1, rows + 1):
    print("* " * i)

# Menu system example
while True:
    print("\n--- Menu ---")
    print("1. Start Game")
    print("2. Settings")
    print("3. Exit")
    choice = input("Choose option: ")
    
    if choice == "1":
        print("Starting game...")
        break
    elif choice == "2":
        print("Opening settings...")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again")