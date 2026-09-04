import psycopg2

# Database configuration
db_name = "db1"
db_password = 1234
db_host = "localhost"
db_user = "postgres"
db_port = 5432

try:
    # Connect to PostgreSQL database
    with psycopg2.connect(
        database=db_name,
        host=db_host,
        user=db_user,
        password=db_password,
        port=db_port
    ) as conn:

        # Create cursor for executing SQL queries
        cursor = conn.cursor()

        # Create student table if it does not already exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS STUDENT_MANAGER(
                ID SERIAL PRIMARY KEY,
                NAME VARCHAR(20),
                MARKS INT
            )
        """)

        # Function to add a student
        def add_student():
            print("1. Add Student")

            name = input("Enter Student name: ")
            marks = int(input("Enter Students marks: "))

            cursor.execute("""
                INSERT INTO STUDENT_MANAGER(NAME, MARKS)
                VALUES(%s, %s)
            """, (name, marks))

            # Save changes to the database
            conn.commit()

            print("Student added successfully")

        # Function to search for a student
        def search_student():
            print("Search student")

            search_name = input("Enter student name to search: ")

            cursor.execute("""
                SELECT * FROM STUDENT_MANAGER
                WHERE NAME = %s
            """, (search_name,))

            row = cursor.fetchall()

            if row:
                for x in row:
                    print(x)
            else:
                print("Student not found")

        # Function to update student marks
        def update_marks():
            print("Update marks")

            search_name = input("Enter student name to search: ")

            cursor.execute("""
                SELECT * FROM STUDENT_MANAGER
                WHERE NAME = %s
            """, (search_name,))

            row = cursor.fetchall()

            if row:
                NEW_MARKS = int(input("Enter new marks to update: "))

                cursor.execute("""
                    UPDATE STUDENT_MANAGER
                    SET MARKS = %s
                    WHERE NAME = %s
                """, (NEW_MARKS, search_name))

                # Save changes to the database
                conn.commit()

                print("Marks updated successfully")
            else:
                print("Student not found")

        # Function to delete a student
        def delete_student():
            print("Delete student")

            d_name = input("Enter Student name to delete: ")

            cursor.execute("""
                SELECT * FROM STUDENT_MANAGER
                WHERE NAME = %s
            """, (d_name,))

            row = cursor.fetchall()

            if row:
                cursor.execute("""
                    DELETE FROM STUDENT_MANAGER
                    WHERE NAME = %s
                """, (d_name,))

                # Save changes to the database
                conn.commit()

                print("Student deleted successfully")
            else:
                print("Student not found")

        # Function to display all students
        def display_students():
            print("Display Students")

            cursor.execute("""
                SELECT * FROM STUDENT_MANAGER
            """)

            row = cursor.fetchall()

            if row:
                for i in row:
                    print(i)
            else:
                print("No data in table")

        # Main menu
        while True:

            print("\nMenu")
            print("1 = Add Student")
            print("2 = Search student")
            print("3 = Update marks")
            print("4 = Delete student")
            print("5 = Display Students")
            print("6 = Exit")

            code = int(input("Enter your choice: "))

            # Handle menu choices using match-case
            match code:

                case 1:
                    add_student()

                case 2:
                    search_student()

                case 3:
                    update_marks()

                case 4:
                    delete_student()

                case 5:
                    display_students()

                case 6:
                    print("End of program")
                    break

                # Handle invalid menu choices
                case _:
                    print("Invalid choice")

except Exception as error:
    # Display any database or program errors
    print(f"Error: {error}")