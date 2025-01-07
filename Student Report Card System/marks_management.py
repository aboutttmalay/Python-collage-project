import sqlite3

class MarksManagement:

    def assign_subjects(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        student_id = input("Enter student ID to assign subjects: ").strip()
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            connection.close()
            return

        subjects = input("Enter subjects separated by commas: ").split(',')

        for subject in subjects:
            try:
                cursor.execute("INSERT INTO subjects (student_id, subject_name) VALUES (?, ?)", (student_id, subject.strip()))
            except sqlite3.IntegrityError:
                print(f"Subject '{subject.strip()}' already assigned to this student.")

        connection.commit()
        connection.close()

        print(f"Subjects assigned for student {student[1]}!")

    def assign_grades(self):
        connection = sqlite3.connect("report_card_system.db")
        cursor = connection.cursor()

        student_id = input("Enter student ID to assign grades: ").strip()
        cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        student = cursor.fetchone()

        if not student:
            print("Student not found.")
            connection.close()
            return

        cursor.execute("SELECT subject_id, subject_name FROM subjects WHERE student_id = ?", (student_id,))
        subjects = cursor.fetchall()

        if not subjects:
            print("No subjects found for this student.")
            connection.close()
            return

        for subject_id, subject_name in subjects:
            grade = input(f"Enter grade for {subject_name}: ").strip()
            marks = int(input(f"Enter marks for {subject_name}: ").strip())
            try:
                cursor.execute(
                    "INSERT INTO marks (student_id, subject_id, grade, marks) VALUES (?, ?, ?, ?)",
                    (student_id, subject_id, grade, marks),
                )
            except sqlite3.IntegrityError:
                cursor.execute(
                    "UPDATE marks SET grade = ?, marks = ? WHERE student_id = ? AND subject_id = ?",
                    (grade, marks, student_id, subject_id),
                )

        connection.commit()
        connection.close()
        print(f"Grades assigned for student {student[1]}!")