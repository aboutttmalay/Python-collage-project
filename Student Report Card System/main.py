from admin_panel import AdminPanel
from marks_management import MarksManagement
from reports import Reports


def main():
    admin_panel = AdminPanel()
    marks_management = MarksManagement()
    reports = Reports()

    while True:
        print("\nStudent Report Card System")
        print("1. Admin Panel")
        print("2. Marks Management")
        print("3. Reports")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            admin_panel.main()
        elif choice == '2':
            marks_management.assign_subjects()
            marks_management.assign_grades()
        elif choice == '3':
            reports.display_student_report()
            reports.view_class_performance()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
