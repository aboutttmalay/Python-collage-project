'''

Program Description: 
School Management System
You are required to develop a School Management System that simulates the key functionalities of managing students, teachers, and courses. The system will use object-oriented programming principles to create models for Students, Teachers, and Courses, with well-defined relationships and functionalities.

Core Features:
User Types:
1. Staff
2. Student

User:
Each student will have:

A unique ID (validated to ensure no duplicates).
A name.
email
phone
address
A list of courses they are enrolled in. []
list of batches assign to the staff--> if the user is student then save this filed as None
A list of courses they teach.

Course Management:

Each course will have:
A unique course ID.
A course name.
course Description
An associated teacher.  []
USER can assign courses to students. [] this will have the list of id's of the student
ID Validation:

The system will validate all user and course IDs to ensure uniqueness before adding them to the database-->  [list of respective Objects].
Functionalities:

Add Users:

Add a new student or teacher to the system with all required details.
Search Users:

Search for a user (student or teacher) by their unique ID.
Assign Courses:

Assign a course to a student and ensure that only a valid teacher is associated with the course.
Display Data:

Show detailed information about a student, including their enrolled courses.
Show detailed information about a teacher, including the courses they teach and their assigned batches.
Classes and Relationships:
Class: Student

Attributes: studentID, name, listOfCourses
Methods: Add course, view courses.
Class: Teacher

Attributes: teacherID, name, listOfCourses, listOfBatches
Methods: Assign course, view courses and batches.
Class: Course

Attributes: courseID, courseName, teacher
Methods: Assign teacher, view course details.
Class: SchoolManagementSystem

Attributes: List of students, teachers, and courses.
Methods:
Add student, teacher, or course.
Validate IDs.
Search users.
Assign courses.
Display details.
Expected Workflow:
Add a teacher or student to the system with their respective details.
Create courses and assign them to teachers.
Enroll students in courses with validation.
Fetch details of a student or teacher using their unique ID.

'''



class School_Management_System:
    def __init__(self):
        self.name = []
        self.unique_ID = 1
        self.email = set()
        self.phone = set()
        self.address = set()
        self.enrollment_no = set()
        self.Courses = []
        self.Unique_course_id = []
        self.Course_name = []
        self.Course_Description = []


    def  display_menu(self):
        print("\nSchool Management System\n")
        print("1. Staff")
        print("2. Student")
    
    def Staff(self):
        name = input("Enter your name: ")
        email = input("Enter the email id:- ")
        phone = int(input("Enter the your phone number: - "))
        address  = input("Enter the address: ")
        enrollment_no = int(input("Enter your enrollment number: "))

        if not name:
            print("Name is required.")
            return
        if not email:
            print("Email is required")
            return
        if not phone:
            print("Phone number is required")
            return
        if not address:
            print("Address is required")
            return
        if  enrollment_no in self.enrollment_no:
            print("Enrollment number must be unique.")
            return
        
        program_stream = self.Course_Management()
        student = {
            "id": self.current_id,
            "name": name,
            "email": email,
            "Address" : self.address,
            "Course" : self.Courses,
            "enrollment_number": self.enrollment_no,
            "program_stream": program_stream
        }   
        self.students.append(student)
        self.email.add(email)
        self.unique_ID+=1
        self.enrollment_no.add(enrollment_no)
        self.address.add(address)
        print("Details add successfully")

    def Course_Management(self):
        print("Choose Course program stream ")
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
        Unique_Course_ID = input("Enter the Course_ID")
        Course_name = input("Enter the Cousre name")
        Course_Description = input("Enter the course_Description")

        course = {
            "ID" : self.Unique_course_id,
            "Course_name" : self.Course_name,
            "Course_Description" : self.Course_Description

        }
        self.Unique_course_id.add(Unique_Course_ID)
        self.Course_name.add(Course_name)
        self.Course_Description.add(Course_Description)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.Staff
            elif choice == '2':
                self.Staff
                break
            else:
                print("Invalid choice. Please try again.")



if __name__ == "__main__":
    system = School_Management_System()
    system.run()