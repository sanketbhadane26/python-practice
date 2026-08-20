# Student Marks Manager

A simple Python console-based Student Marks Manager built while learning Python fundamentals.

## Features

- Add a student and their marks
- Search for a student
- Update student marks
- Delete a student
- Display all students
- Exit the program
- Handles cases where a student is not found

## Concepts Used

- Variables
- Input / Output
- `if-else`
- `while` loop
- Functions
- Dictionaries
- `match-case`
- Dictionary methods
- Basic CRUD operations

## How It Works

The program stores student names and marks in a Python dictionary:

```python
student = {
    "Sanket": 85,
    "Rohit": 90
}
The menu allows the user to perform different operations:

1. Add Student
2. Search Student
3. Update Marks
4. Delete Student
5. Display Students
6. Exit
Example
Student Marks Manager


Do you want to start y/n? y


Menu
1 = Add Student
2 = Search student
3 = Update marks
4 = Delete student
5 = Display Students
6 = Exit


Enter your choice: 1


Enter Student name: Sanket
Enter Students marks: 85
How to Run

Make sure Python is installed.

Run:

python student_marks_manager.py
Future Improvements
Add marks validation (0–100)
Handle invalid input
Prevent duplicate student names
Improve student display format
Add grade calculation
Store student data in a file
Add multiple subjects
Use a database in a future version
