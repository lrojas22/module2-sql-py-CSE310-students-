# Overview

This project is a Student Records Management System developed using Python and MySQL. The software allows users to manage student information through a menu-driven interface. Users can view students, add new students, update student records, delete students, and view student grades and course enrollments.

The application integrates with a MySQL relational database through the `mysql-connector-python` library. SQL queries are executed directly from Python to retrieve and modify data stored in the database.

The purpose of this project was to strengthen my understanding of relational database concepts, SQL queries, and how software applications interact with databases. Through this project, I learned how to perform CRUD operations (Create, Read, Update, Delete), use primary and foreign keys, and retrieve information using JOIN statements.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

This project uses a MySQL relational database named `students_db`.

The database contains three related tables:

### Students

Stores student information.

* student_id (Primary Key)
* first_name
* last_name
* email

### Courses

Stores course information.

* course_id (Primary Key)
* course_name

### Enrollments

Stores the relationship between students and courses.

* enrollment_id (Primary Key)
* student_id (Foreign Key)
* course_id (Foreign Key)
* grade

The Enrollments table links students and courses together and allows grades to be stored for each course enrollment.

# Development Environment

## Tools Used

* Visual Studio Code
* MySQL Workbench
* MySQL Server
* Git and GitHub

## Programming Language and Libraries

* Python 3.13
* mysql-connector-python

The mysql-connector-python library was used to establish a connection between Python and MySQL and execute SQL queries.

# Useful Websites

* https://dev.mysql.com/doc/
* https://www.w3schools.com/mysql/
* https://www.w3schools.com/python/
* https://pypi.org/project/mysql-connector-python/
* https://stackoverflow.com/

# Future Work

* Add course management features (add, update, and delete courses).
* Add student search functionality.
* Create a graphical user interface instead of a console menu.
* Generate reports showing student averages and course statistics.
* Convert the application into a web application using Flask.
