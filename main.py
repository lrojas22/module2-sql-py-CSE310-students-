import mysql.connector

try:
    connection = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password = "l1011267",
        database = "students_db"

    )
    print("Connected to MySQL succesfully")
    

except Exception as e:
    print("Error",e)

cursor = connection.cursor()

def view_students():
    cursor.execute("SELECT * FROM STUDENTS")

    students = cursor.fetchall()
    for student in students:
        print(student)


def add_students():
    
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    query = """INSERT INTO students (first_name, last_name, email)
            VALUES (%s, %s, %s)"""
    cursor.execute(query, (first_name,last_name,email))
    connection.commit()


view_students()
cursor.close()
connection.close()

