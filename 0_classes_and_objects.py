# Classes and Objects - Object-Oriented Programming (OOP)

# Basic class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name} says Woof!")
    
    def get_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

dog1.bark()
dog1.get_info()
dog2.bark()

# Accessing attributes
print(dog1.name)
print(dog1.age)

# Modifying attributes
dog1.age = 4
print(dog1.age)

# Class with more features
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        elif amount <= 0:
            print("Invalid withdrawal amount")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def get_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance

# Using the BankAccount class
account = BankAccount("John", 1000)
account.deposit(500)
account.withdraw(200)
account.get_balance()

# Class variables (shared by all instances)
class Student:
    school = "ABC High School"  # class variable
    
    def __init__(self, name, grade):
        self.name = name      # instance variable
        self.grade = grade
    
    def display_info(self):
        print(f"{self.name} - Grade {self.grade}")
        print(f"School: {Student.school}")

student1 = Student("Alice", 10)
student2 = Student("Bob", 11)

student1.display_info()
student2.display_info()

# Changing class variable
Student.school = "XYZ High School"
student1.display_info()  # both students see the change

# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

cat = Cat("Whiskers")
dog = Dog("Buddy")

cat.speak()
dog.speak()

# Practical example - Library system
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False
    
    def checkout(self):
        if self.is_checked_out:
            print(f"'{self.title}' is already checked out")
        else:
            self.is_checked_out = True
            print(f"'{self.title}' checked out successfully")
    
    def return_book(self):
        if not self.is_checked_out:
            print(f"'{self.title}' is not checked out")
        else:
            self.is_checked_out = False
            print(f"'{self.title}' returned successfully")
    
    def get_info(self):
        status = "Checked out" if self.is_checked_out else "Available"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {status}")

# Using the Book class
book1 = Book("Python Basics", "Peter Sawm", "123-456")
book1.get_info()
book1.checkout()
book1.checkout()  # try again
book1.return_book()

# Another example - Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def display(self):
        print(f"Rectangle: {self.width} x {self.height}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

rect = Rectangle(5, 3)
rect.display()

# Shopping cart example
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})
        print(f"Added {quantity} x {product.name}")
    
    def remove_item(self, product_name):
        for item in self.items:
            if item["product"].name == product_name:
                self.items.remove(item)
                print(f"Removed {product_name}")
                return
        print(f"{product_name} not found in cart")
    
    def get_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total
    
    def display_cart(self):
        print("\n--- Shopping Cart ---")
        for item in self.items:
            prod = item["product"]
            qty = item["quantity"]
            print(f"{prod.name} x {qty} - ${prod.price * qty}")
        print(f"Total: ${self.get_total()}")

# Using shopping cart
cart = ShoppingCart()
apple = Product("Apple", 1.50)
banana = Product("Banana", 0.75)

cart.add_item(apple, 3)
cart.add_item(banana, 2)
cart.display_cart()

# Private attributes (convention: prefix with underscore)
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # "private" by convention
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Invalid age")

person = Person("Peter", 30)
print(person.get_age())
person.set_age(31)
print(person.get_age())