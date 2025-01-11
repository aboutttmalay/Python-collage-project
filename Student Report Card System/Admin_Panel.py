import sqlite3
import hashlib
from database import initialize_database

class AdminPanel:

    def __init__(self):
        initialize_database()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def add_student(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        student_id = input("Enter student ID: ").strip()
        name = input("Enter student name: ").strip()

        try:
            cursor.execute("INSERT INTO students (student_id, name) VALUES (?, ?)", (student_id, name))
            connection.commit()
            print(f"Student {name} added successfully!")
        except sqlite3.IntegrityError:
            print("Student ID already exists. Please use a unique ID.")
        finally:
            connection.close()

    def update_student(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        student_id = input("Enter student ID to update: ").strip()
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            connection.close()
            return

        new_name = input(f"Enter new name for {student[1]}: ").strip()
        cursor.execute("UPDATE students SET name = ? WHERE student_id = ?", (new_name, student_id))
        connection.commit()
        connection.close()

        print(f"Student {new_name} updated successfully!")

    def delete_student(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        student_id = input("Enter student ID to delete: ").strip()
        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        connection.commit()
        connection.close()

        print(f"Student with ID {student_id} deleted successfully!")

    def main(self):
        while True:
            print("\nAdmin Panel")
            print("1. Add Student")
            print("2. Update Student")
            print("3. Delete Student")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.update_student()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    AdminPanel().main()
