import sqlite3
import hashlib
from Admin_Panel import add_student, update_student, assign_grades
from login_pages import hash_password, sign_up, sign_in
from database_files import initialize_database

class StudentReportCardSystem:

    def __init__(self):
        initialize_database()

    

    def display_student_report(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        student_id = input("Enter student ID to view report: ")
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            return

        cursor.execute("SELECT subject_name, grade FROM marks WHERE student_id = ?", (student_id,))
        marks = cursor.fetchall()

        print(f"\nStudent Report for {student[1]}:")
        for subject, grade in marks:
            print(f"{subject}: {grade}")

        connection.close()

    def main(self):
        while True:
            print("\nStudent Report Card System")
            print("1. Sign Up")
            print("2. Sign In")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.sign_up()
            elif choice == '2':
                if self.sign_in():
                    self.run_system()
            elif choice == '3':
                break
            else:
                print("Invalid choice, please try again.")

    def run_system(self):
        while True:
            print("\nStudent Report Card System")
            print("1. Add Student")
            print("2. Update Student")
            print("3. Delete Student")
            print("4. Assign Grades")
            print("5. Display Student Report")
            print("6. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                add_student()
            elif choice == '2':
                update_student()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                assign_grades()
            elif choice == '5':
                self.display_student_report()
            elif choice == '6':
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    StudentReportCardSystem().main()
