import sqlite3

# Initialize the database and tables
def initialize_database():
    connection = sqlite3.connect("report_card_system.db")
    cursor = connection.cursor()

    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL
                      )''')

    # Create students table
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        student_id TEXT PRIMARY KEY,
                        name TEXT NOT NULL
                      )''')

    # Create subjects table
    cursor.execute('''CREATE TABLE IF NOT EXISTS subjects (
                        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id TEXT NOT NULL,
                        subject_name TEXT NOT NULL,
                        FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
                      )''')

    # Create marks table
    cursor.execute('''CREATE TABLE IF NOT EXISTS marks (
                        mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id TEXT NOT NULL,
                        subject_name TEXT NOT NULL,
                        grade TEXT NOT NULL,
                        FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
                      )''')

    connection.commit()
    connection.close()
