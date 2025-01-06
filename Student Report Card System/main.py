import sqlite3

# Initialize the database and tables
def initialize_database():
    connection = sqlite3.connect("report_card_system.db")
    cursor = connection.cursor()

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

class StudentReportCardSystem:

    def __init__(self):
        initialize_database()

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
            print("1. Add Student")
            print("2. Update Student")
            print("3. Delete Student")
            print("4. Assign Grades")
            print("5. Display Student Report")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.update_student()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                self.assign_grades()
            elif choice == '5':
                self.display_student_report()
            elif choice == '6':
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    StudentReportCardSystem().main()
