# If statements - making decisions in code

# Basic if statement
temperature = 30
if temperature > 25:
    print("It's hot outside")
    print("Wear light clothes")

# if-else
age = 17
if age >= 18:
    print("You can vote")
else:
    print("Too young to vote")

# if-elif-else (multiple conditions)
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Nested if statements
has_ticket = True
age = 20
if has_ticket:
    if age >= 18:
        print("Welcome to the concert")
    else:
        print("Sorry, adults only")
else:
    print("Please buy a ticket first")

# Multiple conditions
money = 50
is_weekend = True
if money >= 30 and is_weekend:
    print("Let's go to the movies")

# Checking multiple things
weather = "rainy"
if weather == "sunny" or weather == "cloudy":
    print("Good day for a walk")
else:
    print("Stay inside")

# Real world example - login system
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Invalid credentials")

# Another practical example - discount calculator
purchase_amount = float(input("Enter purchase amount: "))

if purchase_amount >= 100:
    discount = purchase_amount * 0.2  # 20% discount
    print(f"You get 20% off! Discount: ${discount}")
    print(f"Final price: ${purchase_amount - discount}")
elif purchase_amount >= 50:
    discount = purchase_amount * 0.1  # 10% discount
    print(f"You get 10% off! Discount: ${discount}")
    print(f"Final price: ${purchase_amount - discount}")
else:
    print(f"Total: ${purchase_amount}")
    print("Spend $50 or more for a discount!")

# Ternary operator (shorthand if-else)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)