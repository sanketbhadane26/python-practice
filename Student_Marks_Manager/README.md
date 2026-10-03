# Student Marks Manager

A simple Python console-based Student Marks Manager built using **Python and PostgreSQL**.

The project allows users to add, search, update, delete, and display student records through a menu-driven interface.

## Features

* Add a student and their marks
* Search for a student
* Update student marks
* Delete a student
* Display all students
* Automatically generate student IDs
* Handle cases where a student is not found
* Handle invalid menu choices
* Store student data in PostgreSQL
* Separate the project into multiple Python modules

## Concepts Used

* Python Variables
* Input / Output
* `if-else`
* `while` loop
* Functions
* `match-case`
* Exception Handling
* Lists and Dictionaries
* Modular Programming
* PostgreSQL
* `psycopg2`
* SQL Queries
* Parameterized Queries
* Basic CRUD Operations
* Database Transactions using `commit()`

## Project Structure

```text
Student-Marks-Manager/
│
├── main.py
├── student.py
├── database.py
├── utils.py
└── README.md

main.py
Contains the main program flow and menu-driven interface.
Responsible for:
- Displaying the menu
- Taking user input
- Calling the required functions
- Controlling the overall program flow
student.py
Contains student-related operations and logic.
Responsible for:
- Adding students
- Searching students
- Updating student marks
- Deleting students
- Displaying student records
database.py
Handles the PostgreSQL database connection and database-related operations.
Responsible for:
- Connecting to PostgreSQL
- Executing SQL queries
- Managing database operations
- Committing transactions
utils.py
Contains helper functions used by the program.
Responsible for:
- Reusable utility operations
- Input/helper functions
- Keeping the main program cleaner
Database Structure
The program creates a PostgreSQL table named STUDENT_MANAGER:
Column	Type	Description
ID	SERIAL PRIMARY KEY	Automatically generated student ID
NAME	VARCHAR(20)	Student name
MARKS	INT	Student marks


How It Works
The program connects to a PostgreSQL database and provides a menu for performing different operations:
1 = Add Student
2 = Search Student
3 = Update Marks
4 = Delete Student
5 = Display Students
6 = Exit

Example
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

Student added successfully

Display Example
Display Students

(1, 'Sanket', 85)
(2, 'Rohit', 90)

How to Run
1. Make sure Python is installed
Check your Python installation:
python --version

2. Install psycopg2
pip install psycopg2

3. Make sure PostgreSQL is installed and running
Create the database used by the program:
db1

Update the database configuration in database.py if required.
4. Run the program
Run the main Python file:
python main.py

What I Practiced
Through this project, I practiced:
- Breaking a larger Python program into multiple files
- Creating reusable functions
- Working with PostgreSQL
- Connecting Python with a database
- Performing CRUD operations
- Writing SQL queries
- Using parameterized queries
- Handling database transactions
- Organizing code into modules
- Improving code readability and maintainability
Future Improvements
- Add marks validation (0–100)
- Handle invalid numeric input
- Prevent duplicate student names
- Improve student display format
- Add grade calculation
- Add multiple subjects
- Add student attendance
- Add sorting and filtering
- Improve database error handling
- Add a graphical user interface in a future version