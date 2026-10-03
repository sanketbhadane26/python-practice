from student import Student
from database import (
    create_table,
    add_student,
    search_student,
    update_marks,
    delete_student,
    get_all_students
)
from utils import get_name, get_marks
def add_student_menu():
    print("1. Add Student")

    name = get_name()
    marks = get_marks()

    student = Student(name, marks)

    add_student(student)
def search_student_menu():
    print("Search student")

    name = get_name()

    students = search_student(name)

    if students:
        for student in students:
            print(student)
    else:
        print("Student not found")
def update_marks_menu():
    print("Update marks")

    name = get_name()

    students = search_student(name)

    if students:
        new_marks = get_marks()
        update_marks(name, new_marks)

        print("Marks updated successfully")
    else:
        print("Student not found")
def delete_student_menu():
    print("Delete student")

    name = get_name()

    students = search_student(name)

    if students:
        delete_student(name)
        print("Student deleted successfully")
    else:
        print("Student not found")
def display_students_menu():
    print("Display Students")

    students = get_all_students()

    if students:
        for student in students:
            print(student)
    else:
        print("No data in table")
def menu():
    while True:

        print("\nMenu")
        print("1 = Add Student")
        print("2 = Search student")
        print("3 = Update marks")
        print("4 = Delete student")
        print("5 = Display Students")
        print("6 = Exit")

        try:
            choice = int(input("Enter your choice: "))

            match choice:

                case 1:
                    add_student_menu()

                case 2:
                    search_student_menu()

                case 3:
                    update_marks_menu()

                case 4:
                    delete_student_menu()

                case 5:
                    display_students_menu()

                case 6:
                    print("End of program")
                    break

                case _:
                    print("Invalid choice")

        except ValueError:
            print("Please enter a number.")
create_table()
menu()