# Student Marks Manager

A Python console-based Student Marks Manager built using **Python and PostgreSQL**.

The project allows users to add, view, search, update, delete, and analyze student records through a menu-driven interface.

## Features

* Add a student and their marks
* View all students
* Search a student by name
* Search a student by roll number
* Update student marks
* Delete a student
* View student statistics
* Calculate total number of students
* Calculate average marks
* Find the top student
* Automatically generate student roll numbers
* Handle nonexistent students
* Handle invalid marks
* Handle invalid roll numbers
* Handle invalid menu choices
* Handle empty student names
* Store student data in PostgreSQL
* Separate the project into multiple Python modules

## Menu

```text
1. Add Student
2. View Students
3. Search by Name
4. Search by Roll Number
5. Update Student
6. Delete Student
7. Statistics
8. Exit

Concepts Used
- Python Variables
- Input / Output
- if-else
- while loop
- Functions
- match-case
- Exception Handling
- Lists
- Modular Programming
- PostgreSQL
- psycopg2
- SQL Queries
- Parameterized Queries
- CRUD Operations
- Database Transactions
- SQL Aggregate Functions
- Input Validation
Project Structure
Student-Marks-Manager/
│
├── main.py
├── student.py
├── database.py
├── utils.py
├── screenshots/
│   ├── program-running.png
│   ├── database.png
│   ├── search.png
│   └── statistics.png
│
└── README.md

main.py
Contains the main program flow and menu-driven interface.
Responsible for:
- Displaying the menu
- Taking user input
- Calling the required functions
- Handling menu operations
- Controlling the overall program flow
student.py
Contains the Student class.
Responsible for:
- Storing student information
- Storing roll number
- Storing student name
- Storing student marks
database.py
Handles the PostgreSQL database connection and database-related operations.
Responsible for:
- Connecting to PostgreSQL
- Creating the student table
- Adding students
- Searching students
- Searching by roll number
- Updating marks
- Deleting students
- Retrieving all students
- Calculating statistics
- Executing SQL queries
utils.py
Contains helper functions used by the program.
Responsible for:
- Validating student names
- Validating marks
- Validating roll numbers
- Validating menu choices
- Handling invalid input
Database Structure
The program creates a PostgreSQL table named STUDENT_MANAGER.
Column	Type	Description
ID	SERIAL PRIMARY KEY	Automatically generated student roll number
NAME	VARCHAR(20)	Student name
MARKS	INT	Student marks


How It Works
The program connects to a PostgreSQL database and provides a menu for performing different operations.
Add Student
The user enters:
Enter student name: Sanket
Enter student's marks: 85

The student is then stored in the PostgreSQL database.
Search by Name
The user enters a student's name:
Enter student name: Sanket

The program searches the database and displays matching students.
Search by Roll Number
The user enters a roll number:
Enter roll number: 1

The program finds and displays the student associated with that roll number.
Update Student
The user enters the student's roll number and provides new marks.
The program updates the marks in the database.
Delete Student
The user enters the student's roll number.
The program asks for confirmation before deleting the student.
Statistics
The program displays:
Total Students
Average Marks
Top Student

Example:
--- Statistics ---

Total Students: 5
Average Marks: 82.40
Top Student: Sanket
Marks: 95

Invalid Input Handling
The program handles invalid user input without crashing.
Examples include:
Invalid Marks
Enter student's marks: abc

Please enter a valid number.

Marks outside the range 0–100 are also rejected.
Invalid Roll Number
Enter roll number: abc

Please enter a valid roll number.

Empty Name
Enter student name:

Name cannot be empty.

Invalid Menu Choice
Enter your choice: 15

Please enter a choice between 1 and 8.

Student Not Found
Student not found.

Screenshots
Program Running
 
Database
 
Search Student
 
Statistics
 
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
python main.py

What I Practiced
Through this project, I practiced:
- Breaking a larger Python program into multiple files
- Creating reusable functions
- Creating and using a Python class
- Working with PostgreSQL
- Connecting Python with a database
- Performing CRUD operations
- Writing SQL queries
- Using parameterized queries
- Searching database records
- Using SQL aggregate functions
- Handling user input
- Validating user input
- Handling exceptions
- Organizing code into modules
- Improving code readability and maintainability
Future Improvements
- Prevent duplicate student names
- Improve student display format
- Add grade calculation
- Add multiple subjects
- Add student attendance
- Add sorting and filtering
- Improve database error handling
- Add more detailed statistics
- Add a graphical user interface in a future version