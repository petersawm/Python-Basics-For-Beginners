# Practical Projects - Real-world applications

# PROJECT 1: Todo List Manager
class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Added: {task}")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
            return
        
        print("\n--- Your Tasks ---")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["done"] else " "
            print(f"{i}. [{status}] {task['task']}")
    
    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            print(f"Marked as done: {self.tasks[index]['task']}")
        else:
            print("Invalid task number")
    
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number")
    
    def run(self):
        while True:
            print("\n--- Todo List ---")
            print("1. Add task")
            print("2. View tasks")
            print("3. Mark done")
            print("4. Delete task")
            print("5. Exit")
            
            choice = input("Choose: ")
            
            if choice == "1":
                task = input("Enter task: ")
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.view_tasks()
                try:
                    num = int(input("Task number: ")) - 1
                    self.mark_done(num)
                except ValueError:
                    print("Invalid input")
            elif choice == "4":
                self.view_tasks()
                try:
                    num = int(input("Task number: ")) - 1
                    self.delete_task(num)
                except ValueError:
                    print("Invalid input")
            elif choice == "5":
                break

# todo = TodoList()
# todo.run()


# PROJECT 2: Expense Tracker
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self, amount, category, description):
        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)
        print(f"Added expense: ${amount} for {category}")
    
    def view_expenses(self):
        if not self.expenses:
            print("No expenses yet!")
            return
        
        print("\n--- All Expenses ---")
        total = 0
        for i, exp in enumerate(self.expenses, 1):
            print(f"{i}. ${exp['amount']:.2f} - {exp['category']}")
            print(f"   {exp['description']}")
            total += exp['amount']
        print(f"\nTotal: ${total:.2f}")
    
    def view_by_category(self):
        if not self.expenses:
            print("No expenses yet!")
            return
        
        categories = {}
        for exp in self.expenses:
            cat = exp['category']
            if cat not in categories:
                categories[cat] = 0
            categories[cat] += exp['amount']
        
        print("\n--- Expenses by Category ---")
        for cat, amount in categories.items():
            print(f"{cat}: ${amount:.2f}")
    
    def run(self):
        while True:
            print("\n--- Expense Tracker ---")
            print("1. Add expense")
            print("2. View all expenses")
            print("3. View by category")
            print("4. Exit")
            
            choice = input("Choose: ")
            
            if choice == "1":
                try:
                    amount = float(input("Amount: $"))
                    category = input("Category: ")
                    description = input("Description: ")
                    self.add_expense(amount, category, description)
                except ValueError:
                    print("Invalid amount")
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.view_by_category()
            elif choice == "4":
                break

# tracker = ExpenseTracker()
# tracker.run()


# PROJECT 3: Password Manager (simple version)
import json
import os

class PasswordManager:
    def __init__(self, filename="passwords.json"):
        self.filename = filename
        self.passwords = self.load_passwords()
    
    def load_passwords(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}
    
    def save_passwords(self):
        with open(self.filename, 'w') as file:
            json.dump(self.passwords, file, indent=2)
    
    def add_password(self, service, username, password):
        self.passwords[service] = {
            "username": username,
            "password": password
        }
        self.save_passwords()
        print(f"Password saved for {service}")
    
    def get_password(self, service):
        if service in self.passwords:
            info = self.passwords[service]
            print(f"\nService: {service}")
            print(f"Username: {info['username']}")
            print(f"Password: {info['password']}")
        else:
            print("Service not found")
    
    def list_services(self):
        if not self.passwords:
            print("No passwords saved")
            return
        
        print("\n--- Saved Services ---")
        for service in self.passwords:
            print(f"- {service}")
    
    def delete_password(self, service):
        if service in self.passwords:
            del self.passwords[service]
            self.save_passwords()
            print(f"Deleted password for {service}")
        else:
            print("Service not found")

# pm = PasswordManager()
# pm.add_password("Gmail", "user@gmail.com", "password123")
# pm.get_password("Gmail")


# PROJECT 4: Simple Quiz Game
class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"],
                "answer": "B"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
                "answer": "B"
            },
            {
                "question": "Which language is this?",
                "options": ["A. Java", "B. C++", "C. Python", "D. Ruby"],
                "answer": "C"
            }
        ]
        self.score = 0
    
    def play(self):
        print("--- Quiz Game ---")
        print("Answer the questions by typing A, B, C, or D\n")
        
        for i, q in enumerate(self.questions, 1):
            print(f"Question {i}: {q['question']}")
            for option in q['options']:
                print(option)
            
            answer = input("Your answer: ").upper()
            
            if answer == q['answer']:
                print("Correct! ✓\n")
                self.score += 1
            else:
                print(f"Wrong! The answer was {q['answer']}\n")
        
        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")

# quiz = QuizGame()
# quiz.play()


# PROJECT 5: Contact Book
class ContactBook:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, phone, email=""):
        self.contacts[name] = {
            "phone": phone,
            "email": email
        }
        print(f"Contact added: {name}")
    
    def search_contact(self, name):
        if name in self.contacts:
            print(f"\nName: {name}")
            print(f"Phone: {self.contacts[name]['phone']}")
            if self.contacts[name]['email']:
                print(f"Email: {self.contacts[name]['email']}")
        else:
            print("Contact not found")
    
    def list_contacts(self):
        if not self.contacts:
            print("No contacts saved")
            return
        
        print("\n--- All Contacts ---")
        for name, info in self.contacts.items():
            print(f"{name}: {info['phone']}")
    
    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            print(f"Updated contact: {name}")
        else:
            print("Contact not found")
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted contact: {name}")
        else:
            print("Contact not found")

# book = ContactBook()
# book.add_contact("Peter", "555-1234", "peter@email.com")
# book.list_contacts()


# PROJECT 6: Number Statistics Calculator
def calculate_statistics(numbers):
    if not numbers:
        print("No numbers provided")
        return
    
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    
    # Calculate median
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        median = (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    
    print(f"\n--- Statistics ---")
    print(f"Count: {len(numbers)}")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")

# numbers = [5, 2, 8, 1, 9, 3, 7]
# calculate_statistics(numbers)


# PROJECT 7: Text File Analyzer
def analyze_text_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            
        lines = content.split('\n')
        words = content.split()
        characters = len(content)
        
        word_count = {}
        for word in words:
            word = word.lower().strip('.,!?;:')
            word_count[word] = word_count.get(word, 0) + 1
        
        most_common = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]
        
        print(f"\n--- File Analysis: {filename} ---")
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {characters}")
        print(f"\nMost common words:")
        for word, count in most_common:
            print(f"  {word}: {count}")
            
    except FileNotFoundError:
        print(f"File {filename} not found")

# analyze_text_file("sample.txt")