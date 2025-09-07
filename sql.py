import sqlite3

## connect to sqlite
connection=sqlite3.connect("students.db")

## create a cursor object to insert record, 
cursor = connection.cursor()


table_info="""
Create table students(id int, name varchar(20), age int, email varchar(30), department varchar(20), GPA float, GraduationYear int);
"""

cursor.execute(table_info)

#cursor.execute('''Insert into student values('Shalabh','GenAI','A',90)''')
cursor.execute('''
INSERT INTO students (id, Name, age, email, department, GPA, GraduationYear) VALUES
(3336, 'David Palmer', 19, 'sean43@hotmail.com', 'Mathematics', 3.16, 2026),
(8774, 'Andrew Roach', 23, 'vbecker@harvey.com', 'Chemistry', 3.75, 2027),
(1396, 'Jonathan Gonzalez', 22, 'hollydavis@gmail.com', 'Physics', 2.95, 2027),
(6716, 'Kenneth Morrow', 24, 'ganderson@wheeler-atkins.info', 'Physics', 3.55, 2029),
(8830, 'Kaitlyn Martinez', 18, 'hayesdiane@gmail.com', 'Chemistry', 2.29, 2025),
(5305, 'Tiffany Wolf', 23, 'qanderson@taylor.com', 'Mathematics', 3.3, 2029),
(5048, 'James Reyes', 20, 'drodriguez@nguyen-cooper.info', 'Chemistry', 2.44, 2029),
(5986, 'Samantha Sellers', 20, 'michelle27@hubbard-webster.com', 'Mathematics', 3.44, 2025),
(8721, 'Michael Kim', 25, 'jacksonhannah@miles.com', 'Computer Science', 3.27, 2027),
(6622, 'Emily Davis', 18, 'george02@hotmail.com', 'Physics', 3.09, 2030)
''')


#Display all the records

print("The inserted  records are")

data =cursor.execute('''Select * from students''')

for row in data:
    print(row)

    ##Close the connection

connection.commit()
connection.close()