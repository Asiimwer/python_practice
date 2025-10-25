import sqlite3

def create_table():
    conn = sqlite3.connect('portal.db')
    cursor = conn.cursor()
    cursor.execute('''

        CREATE TABLE IF NOT EXISTS user(student_name TEXT NOT NULL,
                   student_age INTEGER NOT NULL,
                   student_class TEXT NOT NULL)

                    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()

class Student():
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"\n Name : {self.name} \n Age : {self.age} \n Grade : {self.grade}")
    def save_to_db(self):
        conn = sqlite3.connect('portal.db')
        cursor = conn.cursor()
        cursor.execute('''

                INSERT OR REPLACE INTO user(student_name,student_age,student_class)
                       VALUES(?,?,?) ''', (self.name,self.age,self.grade))
        conn.commit()
        conn.close()

def save_student():

    st_name = input("Enter name : ")
    st_age = input("Enter Age : ")
    st_grade = input("Enter Grade : ")
    students =  Student(st_name,st_age,st_grade)
    students.display_info()
    students.save_to_db()
    print("Enter '1' to proceed")
    print("Enter '2' to exit")

    proceed = int(input(" Do you want to proceed ? (1/2) : "))
    if proceed !=1:
        return
    

def retrieve_info():
    conn = sqlite3.connect('portal.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    all_students = cursor.fetchall()

    print("All students : ")
    student_value = 0
    for student in all_students:
        student_value +=1
        print(f" \n Student : {student_value}")
        name,age,grade = student

        print(f"\n Name :{name} \n Age : {age} \n Class : {grade}")
    conn.close()

retrieve_info()

def update_user(name_input,new_st_age = None, new_st_grade = None):
    conn = sqlite3.connect('portal.db')
    cursor = conn.cursor()
    if new_st_age and new_st_grade:
        cursor.execute('''
        UPDATE user
        SET student_age = ?,student_class = ?
        WHERE student_name = ? ''', (new_st_age,new_st_grade,name_input) )
    elif new_st_age : 
        cursor.execute('''
        UPDATE user
        SET student_age = ?
        WHERE student_name = ? ''', (new_st_age,name_input))
    elif new_st_grade:
        cursor.execute('''
        UPDATE user
        SET student_class = ?
        WHERE student_name = ? ''', (new_st_grade,name_input))
    conn.commit()
    conn.close()
    print(f"Student {name_input} has successfully been updated")
    retrieve_info()
    
print("Do you want to update student  (1/2) ?")
def update_info():
    update = int(input("Enter '1' to update student : "))
    if int(update) !=1:
        return

    else:
        conn = sqlite3.connect('portal.db')
        cursor = conn.cursor()
        # student_name is my column with student names 
        cursor.execute("SELECT student_name FROM user")
        student_names = [x[0] for x in cursor.fetchall() ]
        name_input = input("Enter name : ")
        if name_input in student_names:
            cursor.execute("SELECT * FROM user where student_name = ? ",(name_input,))
            current_student = cursor.fetchone()
            s_name,s_age,s_grade = current_student
            print(f"Student details : \n Name : {s_name} \n Age: {s_age} \n Class : {s_grade}")
            print("\n Enter '1' for new age")
            print("\n  Enter '2' for new class")
            print("\n Enter 3 for both ")
            print("\n Enter 4 to cancel ")
            new_age= None
            new_grade = None
            update_data = int(input("Enter option : "))
            if update_data ==1:
                new_age = int(input("Enter new age : "))
            elif update_data ==2:
                new_grade = input("Enter new class : ")
            elif update_data ==3:
                new_age = input("Enter new age : ")
                new_grade = input("Enter new class : ")

            update_user(name_input=name_input,new_st_age=new_age,new_st_grade=new_grade)
            conn.close()
            retrieve_info()
update_info()