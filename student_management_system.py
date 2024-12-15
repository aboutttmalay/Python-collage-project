
"""

a program that create a user driven list student management system

use database as dict and list


first list should be shown to the user like:

1. add

functions: add student create new id which should be unique create enrollment number which also should be unique give 
name email (unique) phone address program stream for program and stream give option to choose like

while adding student if ant data is missing the proper message should be displayed for example:
if name is missing then the user should get the message like name is required if email is missing
then then the user should get that email is required  like that



1. b.tech
2. bba
3. mca
4. exit

same for the stream

update the student by  id

update name email phone not the enrollment number and id

delete the student by id

every time validate the id for performing the operations 

like ex:
if user will choose edit student option then 
ask user for id of the student:
then validate the id if the id is correct then update the student 

same for the delete student 

create function for all the operation you can use if else for loop

the program should be dynamic.

create [{},{}]
list of dict for storing the student data

also display all student data in the table format
display one student data by id

user should be able to assign the course to the student  one student can have multiple courses

"""


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.enrollment_numbers = set()
        self.emails = set()
        self.current_id = 1

    def display_menu(self):
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Display Student by ID")
        print("6. Exit")

    def add_student(self):
        
        name = input("Enter Student name: ")
        email = input("Enter Student email: ")
        enrollment_number = input("Enter Enrollment Number: ")

        if not name:
            print("Name is required.")
            return
        if not email:
            print("Email is required.")
            return
        if enrollment_number in self.enrollment_numbers:
            print("Enrollment number must be unique.")
            return
        if email in self.emails:
            print("Email must be unique.")
            return

        program_stream = self.choose_program_stream()

        student = {
            "id": self.current_id,
            "name": name,
            "email": email,
            "enrollment_number": enrollment_number,
            "program_stream": program_stream
        }
        self.students.append(student)
        self.enrollment_numbers.add(enrollment_number)
        self.emails.add(email)
        self.current_id += 1
        print("Student added successfully.")

    def choose_program_stream(self):
        print("Choose program stream:")
        print("1. B.Tech")
        print("2. BBA")
        print("3. MCA")
        choice = input("Enter your choice: ")
        if choice == '1':
            return "B.Tech"
        elif choice == '2':
            return "BBA"
        elif choice == '3':
            return "MCA"
        else:
            print("Invalid choice. Defaulting to 'B.Tech'.")
            return "B.Tech"

    def find_student_by_id(self, student_id):
        return next((student for student in self.students if student['id'] == student_id), None)

    def update_student(self):
        student_id = int(input("Enter student ID to update: "))
        student = self.find_student_by_id(student_id)
        if not student:
            print("Student not found.")
            return

        name = input(f"Enter new name (current: {student['name']}): "). student['name']
        email = input(f"Enter new email (current: {student['email']}): "). student['email']
        if email != student['email'] and email in self.emails:
            print("Email must be unique.")
            return

        student.update({"name": name, "email": email})
        print("Student updated successfully.")

    def delete_student(self):
        student_id = int(input("Enter student ID to delete: "))
        student = self.find_student_by_id(student_id)
        if not student:
            print("Student not found.")
            return

        self.students.remove(student)
        self.enrollment_numbers.remove(student['enrollment_number'])
        self.emails.remove(student['email'])
        print("Student deleted successfully.")

    def display_all_students(self):
        if not self.students:
            print("No students found.")
            return
        print("\nID\tName\tEmail\tEnrollment Number\tProgram Stream")
        for student in self.students:
            print(f"{student['id']}\t{student['name']}\t{student['email']}\t{student['enrollment_number']}\t{student['program_stream']}")

    def display_student_by_id(self):
        student_id = int(input("Enter student ID to display: "))
        student = self.find_student_by_id(student_id)
        if not student:
            print("Student not found.")
            return

        print("\nID:", student['id'])
        print("Name:", student['name'])
        print("Email:", student['email'])
        print("Enrollment Number:", student['enrollment_number'])
        print("Program Stream:", student['program_stream'])

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.update_student()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                self.display_all_students()
            elif choice == '5':
                self.display_student_by_id()
            elif choice == '6':
                print("Exit the program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run()
