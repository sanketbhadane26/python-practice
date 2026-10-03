import psycopg2


db_name = "db1"
db_password = 1234
db_host = "localhost"
db_user = "postgres"
db_port = 5432


def connect_db():
    return psycopg2.connect(
        database=db_name,
        host=db_host,
        user=db_user,
        password=db_password,
        port=db_port
    )
def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS STUDENT_MANAGER(
                ID SERIAL PRIMARY KEY,
                NAME VARCHAR(20),
                MARKS INT
            )
        """)
def add_student(student):
    with connect_db() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO STUDENT_MANAGER(NAME, MARKS)
            VALUES(%s, %s)
        """, (student.name, student.marks))

    print("Student added successfully")
def search_student(name):
    with connect_db() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM STUDENT_MANAGER
            WHERE NAME = %s
        """, (name,))

        return cursor.fetchall()
def update_marks(name, new_marks):
    with connect_db() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE STUDENT_MANAGER
            SET MARKS = %s
            WHERE NAME = %s
        """, (new_marks, name))
def delete_student(name):
    with connect_db() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM STUDENT_MANAGER
            WHERE NAME = %s
        """, (name,))
def get_all_students():
    with connect_db() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM STUDENT_MANAGER
        """)

        return cursor.fetchall()