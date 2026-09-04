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

## Concepts Used

* Python Variables
* Input / Output
* `if-else`
* `while` loop
* Functions
* `match-case`
* Exception Handling
* PostgreSQL
* `psycopg2`
* SQL Queries
* Parameterized Queries
* Basic CRUD Operations
* Database Transactions using `commit()`

## Database Structure

The program creates a PostgreSQL table named `STUDENT_MANAGER`:

| Column | Type               | Description                        |
| ------ | ------------------ | ---------------------------------- |
| ID     | SERIAL PRIMARY KEY | Automatically generated student ID |
| NAME   | VARCHAR(20)        | Student name                       |
| MARKS  | INT                | Student marks                      |

## How It Works

The program connects to a PostgreSQL database and provides a menu for performing different operations:

```text
1 = Add Student
2 = Search Student
3 = Update Marks
4 = Delete Student
5 = Display Students
6 = Exit
```

### Example

```text
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
```

### Display Example

```text
Display Students

(1, 'Sanket', 85)
(2, 'Rohit', 90)
```

## How to Run

### 1. Make sure Python is installed

Check your Python installation:

```bash
python --version
```

### 2. Install psycopg2

```bash
pip install psycopg2
```

### 3. Make sure PostgreSQL is installed and running

Create the database used by the program:

```text
db1
```

Update the database configuration in the Python file if required.

### 4. Run the program

```bash
python student_marks_manager.py
```

## Future Improvements

* Add marks validation (0–100)
* Handle invalid numeric input
* Prevent duplicate student names
* Improve student display format
* Add grade calculation
* Add multiple subjects
* Add student attendance
* Add sorting and filtering
* Improve database error handling
* Add a graphical user interface in a future version
* Separate database operations into a dedicated module
