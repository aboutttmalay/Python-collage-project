import sqlite3
import hashlib

def add_student(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")

        cursor.execute("INSERT INTO students (student_id, name) VALUES (?, ?)", (student_id, name))
        connection.commit()
        connection.close()

        print(f"Student {name} added successfully!")

def update_student(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        student_id = input("Enter student ID to update: ")
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            return

        new_name = input(f"Enter new name for {student[1]}: ")
        cursor.execute("UPDATE students SET name = ? WHERE student_id = ?", (new_name, student_id))
        connection.commit()
        connection.close()

        print(f"Student {new_name} updated successfully!")

def delete_student(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        student_id = input("Enter student ID to delete: ")
        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        connection.commit()
        connection.close()

        print(f"Student with ID {student_id} deleted successfully!")

def assign_grades(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        student_id = input("Enter student ID to assign grades: ")
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            return

        subjects = input("Enter subjects separated by commas: ").split(',')

        for subject in subjects:
            grade = input(f"Enter grade for {subject}: ")
            cursor.execute("INSERT INTO marks (student_id, subject_name, grade) VALUES (?, ?, ?)", (student_id, subject.strip(), grade))

        connection.commit()
        connection.close()

        print(f"Grades assigned for student {student[1]}!")
