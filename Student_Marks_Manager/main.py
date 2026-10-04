from student import Student
import csv
from database import (
    
    create_table,
    add_student,
    search_student,
    search_student_by_roll,
    update_marks,
    delete_student,
    get_all_students,
    get_statistics
)

def export_students_to_csv():
    students = get_all_students()

    if not students:
        print("No students available to export.")
        return

    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Roll No", "Name", "Marks"])

        for student in students:
            writer.writerow(student)

    print("Students exported successfully to students.csv")
from utils import (
    get_name,
    get_marks,
    get_roll_number,
    get_menu_choice
)

def statistics_menu():
    print("\n--- Statistics ---")

    total_students, average_marks, top_student = get_statistics()

    print(f"Total Students: {total_students}")

    if total_students > 0:
        print(f"Average Marks: {average_marks:.2f}")

        print(
            f"Top Student: {top_student[1]} "
            f"(Roll Number: {top_student[0]}, "
            f"Marks: {top_student[2]})"
        )
    else:
        print("No students available for statistics.")
def add_student_menu():
    print("\n--- Add Student ---")

    name = get_name()
    marks = get_marks()

    student = Student(name, marks)

    add_student(student)


def search_by_name_menu():
    print("\n--- Search Student by Name ---")

    name = get_name()

    students = search_student(name)

    if students:
        for student in students:
            print(
                f"Roll Number: {student[0]}, "
                f"Name: {student[1]}, "
                f"Marks: {student[2]}"
            )
    else:
        print("Student not found.")


def search_by_roll_menu():
    print("\n--- Search Student by Roll Number ---")

    roll_number = get_roll_number()

    students = search_student_by_roll(roll_number)

    if students:
        for student in students:
            print(
                f"Roll Number: {student[0]}, "
                f"Name: {student[1]}, "
                f"Marks: {student[2]}"
            )
    else:
        print("Student not found.")


def update_marks_menu():
    print("\n--- Update Student Marks ---")

    roll_number = get_roll_number()

    students = search_student_by_roll(roll_number)

    if students:
        print(
            f"Student: {students[0][1]}, "
            f"Current Marks: {students[0][2]}"
        )

        new_marks = get_marks()

        rows_updated = update_marks(roll_number, new_marks)

        if rows_updated:
            print("Marks updated successfully.")
    else:
        print("Student not found.")


def delete_student_menu():
    print("\n--- Delete Student ---")

    roll_number = get_roll_number()

    students = search_student_by_roll(roll_number)

    if students:
        print(
            f"Student found: "
            f"{students[0][1]} - {students[0][2]} marks"
        )

        confirm = input("Are you sure you want to delete? (y/n): ").strip().lower()

        if confirm == "y":
            delete_student(roll_number)
            print("Student deleted successfully.")

        else:
            print("Deletion cancelled.")

    else:
        print("Student not found.")


def display_students_menu():
    print("\n--- All Students ---")

    students = get_all_students()

    if students:
        for student in students:
            print(
                f"Roll Number: {student[0]}, "
                f"Name: {student[1]}, "
                f"Marks: {student[2]}"
            )
    else:
        print("No students found.")


def statistics_menu():
    print("\n--- Statistics ---")

    total_students, average_marks, top_student = get_statistics()

    print(f"Total Students: {total_students}")

    if total_students > 0:
        print(f"Average Marks: {average_marks:.2f}")

        print(
            f"Top Student: {top_student[1]} "
            f"(Roll Number: {top_student[0]}, "
            f"Marks: {top_student[2]})"
        )

    else:
        print("No students available for statistics.")


def menu():

    while True:

        print("\n========== STUDENT MANAGER ==========")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search by Name")
        print("4. Search by Roll Number")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Statistics")
        print("8. Export Students to CSV")
        print("9. Exit")

        choice = get_menu_choice()

        match choice:

            case 1:
                add_student_menu()

            case 2:
                display_students_menu()

            case 3:
                search_by_name_menu()

            case 4:
                search_by_roll_menu()

            case 5:
                update_marks_menu()

            case 6:
                delete_student_menu()

            case 7:
                statistics_menu()
            case 8:
                export_students_to_csv()

            case 9:
                print("End of program.")
                break


create_table()
menu()