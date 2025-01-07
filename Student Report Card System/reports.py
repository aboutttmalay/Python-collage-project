import sqlite3

class Reports:

    def display_student_report(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        student_id = input("Enter student ID to view report: ").strip()
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            connection.close()
            return

        cursor.execute("SELECT subject_name, grade, marks FROM marks INNER JOIN subjects ON marks.subject_id = subjects.subject_id WHERE marks.student_id = ?", (student_id,))
        marks = cursor.fetchall()

        total_marks = sum(mark[2] for mark in marks) if marks else 0

        print(f"\nStudent Report for {student[1]}:")
        for subject, grade, mark in marks:
            print(f"{subject}: {grade} ({mark} marks)")

        print(f"Total Marks: {total_marks}")
        connection.close()

    def view_class_performance(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        cursor.execute("SELECT student_id, name FROM students")
        students = cursor.fetchall()

        for student_id, name in students:
            cursor.execute("SELECT subject_name, grade, marks FROM marks INNER JOIN subjects ON marks.subject_id = subjects.subject_id WHERE marks.student_id = ?", (student_id,))
            marks = cursor.fetchall()

            total_marks = sum(mark[2] for mark in marks)

            print(f"\nStudent Report for {name}:")
            for subject, grade, mark in marks:
                print(f"{subject}: {grade} ({mark} marks)")

            print(f"Total Marks: {total_marks}")

        connection.close()