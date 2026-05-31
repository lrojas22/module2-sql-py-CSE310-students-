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


#FUNCTIONS
#VIEW ALL STUDENTS
def view_students():
    cursor.execute("SELECT * FROM STUDENTS")

    students = cursor.fetchall()
    for student in students:
        print(student)


#ADD NEW STUDENTS
def add_student():
    
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    query = """INSERT INTO students (first_name, last_name, email)
            VALUES (%s, %s, %s)"""
    cursor.execute(query, (first_name,last_name,email))
    connection.commit()

#UPDATE EMAIL STUDENT
def update_student_email():
    student_id = input("Student Id: ")
    new_email = input("New Email: ")
    query = """
            UPDATE students
            SET email = %s
            WHERE student_id = %s
            """
    cursor.execute(query,(new_email,student_id))
    connection.commit()

#DELETE A STUDENT
def delete_student():
    student_id = input("Student Id: ")
    query = """DELETE FROM students 
            WHERE student_id = %s"""
    cursor.execute(query,(student_id,))
    connection.commit()

def view_students_grades():
    query = """
        SELECT s.first_name, s.last_name, c.course_name, e.grade
        FROM students s JOIN enrollments e
        ON s.student_id = e.student_id
        JOIN courses c
        ON e. course_id = c.course_id
        """
    cursor.execute(query)
    results = cursor.fetchall()

    for result in results:
        print(result)


#PRINCIPAL MENU 

print("MENU")
while True:
    print("\n===== STUDENT RECORDS SYSTEM =====")
    print("1. View Students")
    print("2. Add Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. View Student Grades")
    print("6. Exit")
    try:
        option = int(input("CHOOSE AN OPTION: "))
        if option >= 1 and option <= 6:
            match option:
                case 1:
                    view_students()

                case 2:
                    add_student()
                
                case 3:
                    update_student_email()
                
                case 4:
                    delete_student()

                case 5:
                    view_students_grades()

                case 6:
                    print("GOOD BYE")
                    break
        else :
            print("Enter numbers from 1 to 6")
    except ValueError:
         print("Please enter only numbers from 1 to 6.")
cursor.close()
connection.close()

