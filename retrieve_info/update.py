import sqlite3
conn = sqlite3.connect('portal.db')
cursor = conn.cursor()
# student_name is my column with student names 
cursor.execute("Select student_name from user")
student_names = cursor.fetchmany()
student_names = [x[0] for x in student_names ]
name_input = input("Enter name : ")
if name_input:
    cursor.execute("SELECT * FROM user where student_name = ? ",(name_input,))
    current_student = cursor.fetchone()
    s_name,s_age,s_grade = current_student
    print(f"Student details : \n Name : {s_name} \n Age: {s_age} \n Class : {s_grade}")
else:
    print(f"{name_input} not found")
    
    conn.close()