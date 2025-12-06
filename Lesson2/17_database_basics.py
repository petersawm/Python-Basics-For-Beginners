# Database Basics - Working with SQLite
# SQLite is built into Python, no installation needed

import sqlite3
import os

# Create/Connect to database
def create_connection(db_name="mydatabase.db"):
    try:
        conn = sqlite3.connect(db_name)
        print(f"Connected to {db_name}")
        return conn
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return None

# Create a table
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    
    # SQL command to create table
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER
    )
    """
    
    try:
        cursor.execute(create_table_sql)
        conn.commit()
        print("Table created successfully")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# Insert data
def insert_user(name, email, age):
    conn = create_connection()
    cursor = conn.cursor()
    
    insert_sql = "INSERT INTO users (name, email, age) VALUES (?, ?, ?)"
    
    try:
        cursor.execute(insert_sql, (name, email, age))
        conn.commit()
        print(f"User {name} added successfully")
    except sqlite3.IntegrityError:
        print("Email already exists")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# Insert multiple users
def insert_multiple_users(users):
    conn = create_connection()
    cursor = conn.cursor()
    
    insert_sql = "INSERT INTO users (name, email, age) VALUES (?, ?, ?)"
    
    try:
        cursor.executemany(insert_sql, users)
        conn.commit()
        print(f"Added {len(users)} users")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# Query all data
def get_all_users():
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        
        print("\n--- All Users ---")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")
        
        return users
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()

# Query with condition
def get_user_by_id(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        
        if user:
            print(f"Found: {user[1]} ({user[2]})")
            return user
        else:
            print("User not found")
            return None
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        conn.close()

# Update data
def update_user(user_id, name=None, email=None, age=None):
    conn = create_connection()
    cursor = conn.cursor()
    
    updates = []
    params = []
    
    if name:
        updates.append("name = ?")
        params.append(name)
    if email:
        updates.append("email = ?")
        params.append(email)
    if age:
        updates.append("age = ?")
        params.append(age)
    
    if not updates:
        print("No updates provided")
        conn.close()
        return
    
    params.append(user_id)
    update_sql = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
    
    try:
        cursor.execute(update_sql, params)
        conn.commit()
        print(f"User {user_id} updated")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# Delete data
def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"User {user_id} deleted")
        else:
            print("User not found")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# Search users
def search_users(keyword):
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        sql = "SELECT * FROM users WHERE name LIKE ? OR email LIKE ?"
        cursor.execute(sql, (f"%{keyword}%", f"%{keyword}%"))
        users = cursor.fetchall()
        
        print(f"\n--- Search Results for '{keyword}' ---")
        for user in users:
            print(f"{user[1]} - {user[2]}")
        
        return users
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()

# Working with transactions
def transfer_with_transaction():
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        # Start transaction
        cursor.execute("BEGIN")
        
        # Multiple operations
        cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
        cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
        
        # Commit if all successful
        conn.commit()
        print("Transaction completed")
    except sqlite3.Error as e:
        # Rollback if any error
        conn.rollback()
        print(f"Transaction failed: {e}")
    finally:
        conn.close()

# Database class for better organization
class Database:
    def __init__(self, db_name="app.db"):
        self.db_name = db_name
        self.conn = None
    
    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.conn.row_factory = sqlite3.Row  # Access columns by name
            return self.conn
        except sqlite3.Error as e:
            print(f"Connection error: {e}")
            return None
    
    def close(self):
        if self.conn:
            self.conn.close()
    
    def execute(self, sql, params=()):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, params)
            self.conn.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return None
    
    def fetchall(self, sql, params=()):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, params)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return []

# Practical example: Student management system
class StudentDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        
        # Students table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade TEXT NOT NULL,
            gpa REAL
        )
        """)
        
        # Courses table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_name TEXT NOT NULL,
            score INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
        """)
        
        self.conn.commit()
    
    def add_student(self, name, grade, gpa):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO students (name, grade, gpa) VALUES (?, ?, ?)",
                      (name, grade, gpa))
        self.conn.commit()
        return cursor.lastrowid
    
    def add_course(self, student_id, course_name, score):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO courses (student_id, course_name, score) VALUES (?, ?, ?)",
                      (student_id, course_name, score))
        self.conn.commit()
    
    def get_student_courses(self, student_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT s.name, c.course_name, c.score
        FROM students s
        JOIN courses c ON s.id = c.student_id
        WHERE s.id = ?
        """, (student_id,))
        return cursor.fetchall()
    
    def get_top_students(self, limit=5):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students ORDER BY gpa DESC LIMIT ?", (limit,))
        return cursor.fetchall()
    
    def close(self):
        self.conn.close()

# Using the StudentDatabase
# db = StudentDatabase()
# student_id = db.add_student("Peter Sawm", "10th", 3.8)
# db.add_course(student_id, "Math", 95)
# db.add_course(student_id, "Science", 88)
# courses = db.get_student_courses(student_id)
# print(courses)
# db.close()

# Backup database
def backup_database(source_db, backup_db):
    try:
        source = sqlite3.connect(source_db)
        backup = sqlite3.connect(backup_db)
        source.backup(backup)
        backup.close()
        source.close()
        print(f"Backup created: {backup_db}")
    except sqlite3.Error as e:
        print(f"Backup failed: {e}")

# Export to CSV
def export_to_csv(db_name, table_name, csv_filename):
    import csv
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    # Get column names
    column_names = [description[0] for description in cursor.description]
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)
        writer.writerows(rows)
    
    conn.close()
    print(f"Exported to {csv_filename}")

# Import from CSV
def import_from_csv(db_name, table_name, csv_filename):
    import csv
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    with open(csv_filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            columns = ', '.join(row.keys())
            placeholders = ', '.join(['?' for _ in row])
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            
            cursor.execute(sql, list(row.values()))
    
    conn.commit()
    conn.close()
    print(f"Imported from {csv_filename}")

# Check if table exists
def table_exists(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT name FROM sqlite_master 
    WHERE type='table' AND name=?
    """, (table_name,))
    
    exists = cursor.fetchone() is not None
    conn.close()
    
    return exists