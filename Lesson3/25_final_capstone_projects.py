# Final Capstone Projects - Complete applications combining multiple concepts

# PROJECT 1: Advanced Todo App with Database
import sqlite3
from datetime import datetime

class TodoApp:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_table()
    
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority INTEGER DEFAULT 1,
            completed BOOLEAN DEFAULT 0,
            created_at TEXT,
            completed_at TEXT
        )
        ''')
        self.conn.commit()
    
    def add_task(self, title, description="", priority=1):
        cursor = self.conn.cursor()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
        INSERT INTO tasks (title, description, priority, created_at)
        VALUES (?, ?, ?, ?)
        ''', (title, description, priority, created_at))
        self.conn.commit()
        print(f"Task added: {title}")
    
    def list_tasks(self, show_completed=False):
        cursor = self.conn.cursor()
        if show_completed:
            cursor.execute("SELECT * FROM tasks ORDER BY priority DESC, id")
        else:
            cursor.execute("SELECT * FROM tasks WHERE completed=0 ORDER BY priority DESC, id")
        
        tasks = cursor.fetchall()
        if not tasks:
            print("No tasks found")
            return
        
        print("\n" + "="*60)
        for task in tasks:
            status = "✓" if task[4] else "○"
            print(f"{status} [{task[0]}] {task[1]} (Priority: {task[3]})")
            if task[2]:
                print(f"    {task[2]}")
        print("="*60)
    
    def complete_task(self, task_id):
        cursor = self.conn.cursor()
        completed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
        UPDATE tasks SET completed=1, completed_at=? WHERE id=?
        ''', (completed_at, task_id))
        self.conn.commit()
        print(f"Task {task_id} marked as completed")
    
    def delete_task(self, task_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        self.conn.commit()
        print(f"Task {task_id} deleted")
    
    def search_tasks(self, keyword):
        cursor = self.conn.cursor()
        cursor.execute('''
        SELECT * FROM tasks WHERE title LIKE ? OR description LIKE ?
        ''', (f"%{keyword}%", f"%{keyword}%"))
        
        tasks = cursor.fetchall()
        if tasks:
            for task in tasks:
                print(f"[{task[0]}] {task[1]}")
        else:
            print("No tasks found")
    
    def close(self):
        self.conn.close()


# PROJECT 2: Budget Tracker with Reports
class BudgetTracker:
    def __init__(self):
        self.conn = sqlite3.connect('budget.db')
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT,
            date TEXT NOT NULL
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            category TEXT PRIMARY KEY,
            limit_amount REAL NOT NULL
        )
        ''')
        
        self.conn.commit()
    
    def add_transaction(self, type, category, amount, description=""):
        cursor = self.conn.cursor()
        date = datetime.now().strftime("%Y-%m-%d")
        
        cursor.execute('''
        INSERT INTO transactions (type, category, amount, description, date)
        VALUES (?, ?, ?, ?, ?)
        ''', (type, category, amount, description, date))
        
        self.conn.commit()
        print(f"{type} of ${amount} added to {category}")
        
        if type == "expense":
            self.check_budget(category)
    
    def set_budget(self, category, limit):
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT OR REPLACE INTO budgets (category, limit_amount)
        VALUES (?, ?)
        ''', (category, limit))
        self.conn.commit()
        print(f"Budget set for {category}: ${limit}")
    
    def check_budget(self, category):
        cursor = self.conn.cursor()
        
        # Get budget limit
        cursor.execute("SELECT limit_amount FROM budgets WHERE category=?", (category,))
        budget = cursor.fetchone()
        
        if not budget:
            return
        
        # Get total expenses
        cursor.execute('''
        SELECT SUM(amount) FROM transactions
        WHERE category=? AND type='expense'
        AND strftime('%Y-%m', date) = strftime('%Y-%m', 'now')
        ''', (category,))
        
        total = cursor.fetchone()[0] or 0
        limit = budget[0]
        
        if total > limit:
            print(f"⚠️ WARNING: Over budget for {category}!")
            print(f"   Spent: ${total:.2f} / Limit: ${limit:.2f}")
        elif total > limit * 0.8:
            print(f"⚠️ Note: 80% of budget used for {category}")
    
    def monthly_report(self):
        cursor = self.conn.cursor()
        
        # Income
        cursor.execute('''
        SELECT SUM(amount) FROM transactions
        WHERE type='income'
        AND strftime('%Y-%m', date) = strftime('%Y-%m', 'now')
        ''')
        income = cursor.fetchone()[0] or 0
        
        # Expenses
        cursor.execute('''
        SELECT SUM(amount) FROM transactions
        WHERE type='expense'
        AND strftime('%Y-%m', date) = strftime('%Y-%m', 'now')
        ''')
        expenses = cursor.fetchone()[0] or 0
        
        # By category
        cursor.execute('''
        SELECT category, SUM(amount) FROM transactions
        WHERE type='expense'
        AND strftime('%Y-%m', date) = strftime('%Y-%m', 'now')
        GROUP BY category
        ''')
        by_category = cursor.fetchall()
        
        print("\n" + "="*50)
        print("MONTHLY REPORT")
        print("="*50)
        print(f"Total Income:   ${income:.2f}")
        print(f"Total Expenses: ${expenses:.2f}")
        print(f"Net:            ${income - expenses:.2f}")
        print("\nExpenses by Category:")
        for cat, amount in by_category:
            print(f"  {cat}: ${amount:.2f}")
        print("="*50)
    
    def close(self):
        self.conn.close()


# PROJECT 3: Student Grade Management System
class GradeManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self, student_id, name):
        if student_id in self.students:
            print("Student already exists")
            return
        
        self.students[student_id] = {
            'name': name,
            'grades': {}
        }
        print(f"Student added: {name}")
    
    def add_grade(self, student_id, subject, grade):
        if student_id not in self.students:
            print("Student not found")
            return
        
        self.students[student_id]['grades'][subject] = grade
        print(f"Grade added for {self.students[student_id]['name']}")
    
    def calculate_gpa(self, student_id):
        if student_id not in self.students:
            return None
        
        grades = self.students[student_id]['grades'].values()
        if not grades:
            return 0
        
        return sum(grades) / len(grades)
    
    def get_student_report(self, student_id):
        if student_id not in self.students:
            print("Student not found")
            return
        
        student = self.students[student_id]
        print(f"\nStudent Report: {student['name']}")
        print("="*40)
        
        for subject, grade in student['grades'].items():
            print(f"{subject}: {grade}")
        
        gpa = self.calculate_gpa(student_id)
        print(f"\nGPA: {gpa:.2f}")
        print("="*40)
    
    def class_statistics(self):
        if not self.students:
            print("No students")
            return
        
        all_gpas = [self.calculate_gpa(sid) for sid in self.students]
        
        print("\nClass Statistics")
        print("="*40)
        print(f"Total Students: {len(self.students)}")
        print(f"Average GPA: {sum(all_gpas)/len(all_gpas):.2f}")
        print(f"Highest GPA: {max(all_gpas):.2f}")
        print(f"Lowest GPA: {min(all_gpas):.2f}")
        
        # Top students
        sorted_students = sorted(
            self.students.items(),
            key=lambda x: self.calculate_gpa(x[0]),
            reverse=True
        )
        
        print("\nTop 3 Students:")
        for i, (sid, data) in enumerate(sorted_students[:3], 1):
            gpa = self.calculate_gpa(sid)
            print(f"{i}. {data['name']} - GPA: {gpa:.2f}")


# PROJECT 4: Simple Banking System
class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
        self.transactions = []
        self._add_transaction("Account opened", initial_balance)
    
    def _add_transaction(self, type, amount):
        transaction = {
            'type': type,
            'amount': amount,
            'balance': self.balance,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transactions.append(transaction)
    
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return False
        
        self.balance += amount
        self._add_transaction("Deposit", amount)
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return False
        
        if amount > self.balance:
            print("Insufficient funds")
            return False
        
        self.balance -= amount
        self._add_transaction("Withdrawal", -amount)
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            self._add_transaction(f"Transfer to {target_account.account_number}", -amount)
            target_account._add_transaction(f"Transfer from {self.account_number}", amount)
            print(f"Transferred ${amount:.2f} to {target_account.holder_name}")
            return True
        return False
    
    def get_statement(self):
        print(f"\nAccount Statement: {self.holder_name}")
        print(f"Account #: {self.account_number}")
        print("="*60)
        
        for trans in self.transactions[-10:]:  # Last 10 transactions
            print(f"{trans['timestamp']} | {trans['type']}: ${abs(trans['amount']):.2f} | Balance: ${trans['balance']:.2f}")
        
        print("="*60)
        print(f"Current Balance: ${self.balance:.2f}")

class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1000
    
    def create_account(self, holder_name, initial_deposit=0):
        account_number = str(self.next_account_number)
        self.next_account_number += 1
        
        account = BankAccount(account_number, holder_name, initial_deposit)
        self.accounts[account_number] = account
        
        print(f"Account created for {holder_name}")
        print(f"Account Number: {account_number}")
        return account_number
    
    def get_account(self, account_number):
        return self.accounts.get(account_number)


# PROJECT 5: Inventory Management System
class InventorySystem:
    def __init__(self):
        self.products = {}
        self.next_id = 1
    
    def add_product(self, name, price, quantity):
        product_id = f"P{self.next_id:04d}"
        self.next_id += 1
        
        self.products[product_id] = {
            'name': name,
            'price': price,
            'quantity': quantity
        }
        
        print(f"Product added: {name} (ID: {product_id})")
        return product_id
    
    def update_quantity(self, product_id, quantity_change):
        if product_id not in self.products:
            print("Product not found")
            return False
        
        self.products[product_id]['quantity'] += quantity_change
        
        if self.products[product_id]['quantity'] < 0:
            print("Insufficient stock")
            self.products[product_id]['quantity'] -= quantity_change
            return False
        
        print(f"Quantity updated. New stock: {self.products[product_id]['quantity']}")
        return True
    
    def get_inventory_value(self):
        total = sum(
            p['price'] * p['quantity']
            for p in self.products.values()
        )
        return total
    
    def low_stock_report(self, threshold=10):
        print("\nLow Stock Items:")
        print("="*50)
        
        low_stock = {
            pid: p for pid, p in self.products.items()
            if p['quantity'] < threshold
        }
        
        if not low_stock:
            print("All items have sufficient stock")
            return
        
        for pid, product in low_stock.items():
            print(f"{pid}: {product['name']} - Only {product['quantity']} left")
    
    def inventory_report(self):
        print("\nFull Inventory Report")
        print("="*60)
        
        for pid, product in self.products.items():
            value = product['price'] * product['quantity']
            print(f"{pid}: {product['name']}")
            print(f"  Price: ${product['price']:.2f} | Qty: {product['quantity']} | Value: ${value:.2f}")
        
        print("="*60)
        print(f"Total Inventory Value: ${self.get_inventory_value():.2f}")


# USAGE EXAMPLES (commented out - uncomment to run)

"""
# Todo App
app = TodoApp()
app.add_task("Learn Python", "Complete all tutorials", priority=3)
app.add_task("Build project", "Create a web app", priority=2)
app.list_tasks()
app.complete_task(1)
app.close()

# Budget Tracker
tracker = BudgetTracker()
tracker.set_budget("Food", 500)
tracker.add_transaction("expense", "Food", 150, "Groceries")
tracker.add_transaction("income", "Salary", 3000, "Monthly salary")
tracker.monthly_report()
tracker.close()

# Grade Manager
gm = GradeManager()
gm.add_student("S001", "Peter Sawm")
gm.add_grade("S001", "Math", 95)
gm.add_grade("S001", "Science", 88)
gm.get_student_report("S001")

# Banking System
bank = Bank()
acc1 = bank.create_account("Peter Sawm", 1000)
acc2 = bank.create_account("Jane Smith", 500)
account1 = bank.get_account(acc1)
account2 = bank.get_account(acc2)
account1.transfer(account2, 200)
account1.get_statement()

# Inventory System
inv = InventorySystem()
inv.add_product("Laptop", 999.99, 50)
inv.add_product("Mouse", 29.99, 5)
inv.low_stock_report()
inv.inventory_report()
"""