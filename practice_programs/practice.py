import psycopg2
db_name="db1"
db_password=1234
db_host="localhost"
db_user="postgres"
db_port=5432
try:
    with psycopg2.connect(
        database=db_name,
        host=db_host,
        user=db_user,
        password=db_password,
        port=db_port
    )as conn:
        cursor=conn.cursor()
        cursor.execute("""
        select * from table1
""")
        rows=cursor.fetchall()
        for i in rows:
            print(rows)
        
except Exception as error:
    print(f"Error {error}")