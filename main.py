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
cursor.execute("SELECT * FROM STUDENTS")

students = cursor.fetchall()
for student in students:
    print(student)

cursor.close()
connection.close()