import sqlite3

def initialize_database():
    connection = sqlite3.connect("report_card_system.db")
    cursor = connection.cursor()

    # Enable foreign key constraints
    cursor.execute("PRAGMA foreign_keys = ON;")

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
                        UNIQUE(student_id, subject_name),
                        FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
                      )''')

    # Drop marks table if it exists and create it again
    cursor.execute("DROP TABLE IF EXISTS marks;")
    cursor.execute('''CREATE TABLE marks (
                        mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id TEXT NOT NULL,
                        subject_id INTEGER NOT NULL,
                        grade TEXT NOT NULL,
                        marks INTEGER NOT NULL,
                        FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
                        FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE
                      )''')

    connection.commit()
    connection.close()