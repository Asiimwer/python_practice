import sqlite3

conn = sqlite3.connect('student_portal.db')
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS student(student_no TEXT PRIMARY KEY,
               student_name TEXT NOT NULL,
               student_gender TEXT NOT NULL,
               student_dob INTEGER NOT NULL,
               student_campus TEXT NOT NULL,
               student_status TEXT NOT NULL,
               student_class TEXT NOT NULL,
               student_course_1 TEXT NOT NULL,
               student_course_2 TEXT,
               c1_grades TEXT,
               c2_grades TEXT)
               ''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturer(staff_no TEXT PRIMARY KEY,
               staff_name TEXT NOT NULL,
               staff_gender TEXT NOT NULL,
               staff_dob INTEGER NOT NULL,
               staff_campus TEXT NOT NULL,
               staff_status TEXT NOT NULL,
               staff_department TEXT NOT NULL,
               staff_student_lists TEXT)
               ''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin(admin_no TEXT PRIMARY KEY,
               admin_name TEXT NOT NULL,
               admin_gender TEXT NOT NULL,
               admin_role TEXT NOT NULL,
               admin_campus TEXT NOT NULL,
               admin_status TEXT NOT NULL,
               admin_password TEXT NOT NULL)
               ''')

conn.commit()
conn.close()

class Person():
    def __init__(self,names,gender,dob = None,campus= None,status=None):
        self.names = names
        self.gender = gender
        self.dob = dob
        self.campus = campus
        self.status = status

    def describe_role(self):
        print(f"My name is {self.names} I am a {self.status}")

class Administrator():
    def check_student(self,student_number):
        conn = sqlite3.connect('student_portal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        all_students = [ x[0] for x in cursor.fetchall()]
        if student_number in all_students:
            cursor.execute("SELECT *FROM student WHERE student_no = ?",(student_number,))
            student_info = cursor.fetchone()
            return student_info
            # print(f"\n Names : {names} \n Gender : {gender} \n  Dob : {dob} \n campus : {campus} \n Status : {status} \n Class : {s_class} \n Course 1 : {course_1} \n Grade : {c1_grade} \n  Course 2 : {course_2} \n Grade : {c2_grade}")
        else: 
            conn.close()
            return None
        

    def add_course(self):
        student_no = input("Input student number : ")
        student_search = self.check_student(student_no)
        if student_search:
            conn = sqlite3.connect("student_portal.db")
            cursor = conn.cursor()
            print("Student found")
            names,gender,dob,campus,status,s_class,course_1,course_2,c1_grade,c2_grade = student_search
            print(f"\n Names : {names} \n Gender : {gender} \n  Dob : {dob} \n campus : {campus} \n Status : {status} \n Class : {s_class} \n Course 1 : {course_1} \n Grade : {c1_grade} \n  Course 2 : {course_2} \n Grade : {c2_grade}")
            add_course = int(input("Add Course 1/ Course 2 (1/2) : "))
            if add_course == 1:
                print("Course 1:")
                new_course = input("\n Enter course name : ")
                cursor.execute('''
                        UPDATE student
                        SET student_course_1 = ? 
                        WHERE student_no = ? ''', (new_course,student_no) )
            elif add_course ==2:
                print("Course 2:")
                new_course = input("\n Enter course name : ")
                cursor.execute('''
                        UPDATE student
                        SET student_course_2 = ?
                        WHERE student_no = ? ''', (new_course, student_no))
            conn.commit()
            conn.close()
    def assign_grade(self):
        conn = sqlite3.connect("student_portal.db")
        cursor = conn.cursor()

        student_no = input("Enter Student number : ")
        student_search = self.check_student(student_no)  # I assume this returns True/False

        if student_search:
            cursor.execute("SELECT * FROM student WHERE student_no = ?", (student_no,))
            student_search = cursor.fetchone()

            if student_search is None:
                print("Student not found in DB!")
                conn.close()
                return

            student_no, names, gender, dob, campus, status, s_class, course_1, c1_grade, course_2, c2_grade = student_search

            print(f"\n Names : {names} \n Gender : {gender} \n Dob : {dob} \n Campus : {campus} \n Status : {status} \n Class : {s_class} \n Course 1 : {course_1} \n Grade : {c1_grade} \n Course 2 : {course_2} \n Grade : {c2_grade}")

            assign_grade = int(input(f"Assign grade for {course_1} / {course_2} (1/2) : "))
            new_grade = input(f"Assign grade : ")

            if assign_grade == 1:
                cursor.execute("UPDATE student SET c1_grades = ? WHERE student_no = ?", (new_grade, student_no))
                print(f"Grade changed to {new_grade}")
            elif assign_grade == 2:
                cursor.execute("UPDATE student SET c2_grades = ? WHERE student_no = ?", (new_grade, student_no))
                print(f"Grade changed to {new_grade}")
            print(f"\n Names : {names} \n Gender : {gender} \n Dob : {dob} \n Campus : {campus} \n Status : {status} \n Class : {s_class} \n Course 1 : {course_1} \n Grade : {c1_grade} \n Course 2 : {course_2} \n Grade : {c2_grade}")

        conn.commit()
        conn.close()


    def generate_report(self):
        conn = sqlite3.connect("student_portal.db")
        cursor = conn.cursor()
        print("Report generation")
        student_no = input("Input student number : ")
        student_search = self.check_student(student_no)
        if student_search:
            generate_report = int(input("Insert '1' to generate report. Insert '2' to cancel : "))
            if generate_report == 1:
                cursor.execute("SELECT * FROM student WHERE student_no = ?", (student_no,))
                student_search = cursor.fetchone()
                student_no,names,gender,dob,campus,status,s_class,course_1,course_2,c1_grade,c2_grade = student_search
                print(f"\n Student Number : {student_no} \n Names : {names} \n Gender : {gender} \n  Dob : {dob} \n campus : {campus} \n Status : {status} \n Class : {s_class} \n Course 1 : {course_1} \n Grade : {c1_grade} \n  Course 2 : {course_2} \n Grade : {c2_grade}")
        conn.commit()
        conn.close()
    def generate_student_no(self):
        conn = sqlite3.connect('student_portal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT student_no FROM student ORDER BY student_no DESC LIMIT 1")
        last = cursor.fetchone()
        if last is None or last[0] is None:
            new_id = 'ST001'
        else:
            last_id = last[0]
            number = int(last_id[2:])+1
            new_id = f"ST{number:03d}"
        conn.commit()
        conn.close()
        return new_id    
    def register_student(self):
        print("Student registration")
        st_names=input("Enter student name : ")
        st_gender =input("Enter student gender : ")
        st_dob =input("Enter student DOB : ")
        st_campus =input("Enter student campus : ")
        st_status =input("Enter student status : ")
        st_class =input("Enter student Class : ")
        st_course_1 =input("Enter student Course 1 : ")
        st_c1_grade =input("Enter student Course 1 Grade : ")
        st_course_2=input("Enter student Course 2 : ")
        st_c2_grade=input("Enter student Course 2 Grade : ")
        student_no = self.generate_student_no()
        new_student = Student(student_no,st_names,st_gender,st_dob,st_campus,st_status,st_class,st_course_1,st_c1_grade,st_course_2,st_c2_grade)
        new_student.student_to_db()
        print("Student Registered !!")

    def register_lecturer(self):
        print("Lecturer registration")
        lc_names=input("Enter lecturer name : ")
        lc_gender =input("Enter lecturer gender : ")
        lc_dob =input("Enter lecturer DOB : ")
        lc_campus =input("Enter lecturer campus : ")
        lc_status =input("Enter lecturer status : ")
        lc_department = input("Enter lecturer department : ")
        new_lecturer = Lecturer(lc_names,lc_gender,lc_dob,lc_campus,lc_status,lc_department)
        new_lecturer.lect_to_db()
        print("Lecturer registered !!")

    def verification(self):
        conn = sqlite3.connect('student_portal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin")
        admin_numbers =[ x[0] for x in cursor.fetchall()]
        ad_no = input("Input admin no : ")
        if ad_no:
            if ad_no in admin_numbers:
                cursor.execute("SELECT admin_password FROM admin WHERE admin_no = ?",(ad_no,))
                admin_password = cursor.fetchone()
                stored_password = admin_password[0]
                key = input("Input Admin password : ")
                if key == stored_password:
                    return True
                else: print("Incorrect password")
        else: 
            print("Username not found ") 

        

    def main_operator(self):
        print("Enter '1' to check student")
        print("Enter '2' to assign grade")
        print("Enter '3' to generate report")
        print("Enter '4' to register student ")
        print("Enter '5' to  register lecturer ")
        print("Enter '6' to add admin")
        user_input = int(input("Enter option : "))
        if user_input == 1:
            verification = self.verification()
            if verification :
                self.check_student()
        elif user_input == 2:
            verification = self.verification()
            if verification:
                self.assign_grade()
        elif user_input == 3:
            verification = self.verification()
            if verification:
              self.generate_report()
        elif user_input == 4:
            verification = self.verification()
            if verification:
                self.register_student()
        elif user_input == 5:
            verification = self.verification()
            if verification:
             self.register_lecturer()
        elif user_input==6:
            verification = self.verification()
            if verification:
                Admin.add_admin(self)
        else:
            self.verification()
       

class Admin():
    def __init__(self, admin_no, names, gender,status, campus, role,password):
        self.names = names
        self.gender = gender
        self.password= password
        self.admin_no = admin_no
        self.role = role
        self.status = status
        self.campus = campus
    def admin_to_db(self):
        conn = sqlite3.connect('student_portal.db')
        cursor = conn.cursor()
        cursor.execute('''
                INSERT OR REPLACE INTO admin(admin_no,admin_name,admin_gender,admin_role,admin_campus,admin_status,admin_password)
                     VALUES(?,?,?,?,?,?,?)''' , (self.admin_no,self.names,self.gender,self.role,self.campus,self.status,self.password))        
        conn.commit()
        conn.close()
    def add_admin(self):
        print("Input admin details")
        admin_no = input("Enter admin number : ")
        admin_names = input("Enter name : ")
        admin_gender = input("Input gender : ")
        admin_role = input("Input Role : ")
        admin_campus = input("Enter campus : ")
        admin_status = input("Input status : ")
        admin_password = input("Input Admin Password : ")
        new_admin = Admin(admin_no,admin_names,admin_gender,admin_role,admin_campus,admin_status,admin_password)
        new_admin.admin_to_db()
        if new_admin:
            print("Admin added successfully :")
class Student(Person):
    def __init__(self,student_no,names, gender, dob, campus, status,student_class,course_1,c1_grade = None,course_2=None,c2_grade=None):
        self.student_no = student_no
        self.student_class = student_class
        self.course_1 = course_1
        self.c1_grade  = c1_grade
        self.course_2 = course_2
        self.c2_grade = c2_grade
        super().__init__(names, gender, dob, campus, status)
    def describe_role(self):
        return super().describe_role()
  

    def student_to_db(self):
        conn = sqlite3.connect('student_portal.db')
        cursor = conn.cursor()
        cursor.execute('''
                INSERT OR REPLACE INTO student(student_no,student_name,student_gender,student_dob,student_campus,student_status,student_class,student_course_1,c1_grades,student_course_2,c2_grades)
                VALUES (?,?,?,?,?,?,?,?,?,?,?) ''', (self.student_no,self.names,self.gender,self.dob,self.campus,self.status,self.student_class,self.course_1,self.c1_grade,self.course_2,self.c2_grade))
        conn.commit()
        conn.close()
class Lecturer(Person,Administrator) :
    def __init__(self, names, gender, dob, campus, status,department,student_list = None):
        self.department = department
        self.student_list = student_list
        super().__init__(names, gender, dob, campus, status)
    def describe_role(self):
        return super().describe_role()
    def lect_to_db(self):
        conn = sqlite3.connect('student_portal.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO lecturer(staff_name,staff_gender,staff_dob,staff_campus,staff_status,staff_department,staff_student_lists)
                       VALUES(?,?,?,?,?,?,?)''',(self.names,self.gender,self.dob,self.campus,self.status,self.department,self.student_list))
        conn.commit()
        conn.close()      

if __name__ == "__main__":
    admin = Administrator()
    admin.main_operator()
    