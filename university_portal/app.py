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
conn.commit()
conn.close()

class Person():
    def __init__(self,names,gender,dob,campus,status):
        self.names = names
        self.gender = gender
        self.dob = dob
        self.campus = campus
        self.status = status

    def describe_role(self):
        print(f"My name is {self.names} I am a {self.status}")

class Administrator():
    def check_student(self):
        conn = sqlite3.connect('student_portal.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        all_students = [ x[0] for x in cursor.fetchall()]
        student_number = input("Input student number : ")
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
                        SET student_course_2 ?
                        WHERE student_no = ? ''', new_course, student_no)
            conn.commit()
            conn.close()
    def assign_grade(self):
        conn = sqlite3.connect("student_portal.db")
        cursor = conn.cursor()
        student_no = input("Enter Student number : ")
        student_search = self.check_student(student_no)
        if student_search :
            student_search = cursor.execute("SELECT * FROM student WHERE student_no = ?", (student_no,))
            names,gender,dob,campus,status,s_class,course_1,course_2,c1_grade,c2_grade = student_search
            print(f"\n Names : {names} \n Gender : {gender} \n  Dob : {dob} \n campus : {campus} \n Status : {status} \n Class : {s_class} \n Course 1 : {course_1} \n Grade : {c1_grade} \n  Course 2 : {course_2} \n Grade : {c2_grade}")
            assign_grade = int(input(f"Assign grade for {course_1} / {course_2} (1/2) : "))
            if assign_grade==1:
                new_grade=input(f"Assign grade for {course_1} :")
                cursor.execute('''
                        UPDATE student
                        SET c1_grade = ?
                        WHERE student_no = ?''', (new_grade,student_no))
            elif assign_grade == 2:
                cursor.execute('''
                            UPDATE student
                               SET c2_grade = ?
                               WHERE student_no = ? ''', (new_grade,student_no))
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
                student_search = cursor.execute("SELECT * FROM student WHERE student_no = ?", (student_no,))
                names,gender,dob,campus,status,s_class,course_1,course_2,c1_grade,c2_grade = student_search
                print(f"\n Names : {names} \n Gender : {gender} \n  Dob : {dob} \n campus : {campus} \n Status : {status} \n Class : {s_class} \n Course 1 : {course_1} \n Grade : {c1_grade} \n  Course 2 : {course_2} \n Grade : {c2_grade}")
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


    def main_operator(self):
        print("Enter '1' to check student")
        print("Enter '2' to assign grade")
        print("Enter '3' to generate report")
        print("Enter '4' to register student ")
        print("Enter '5' to  register lecturer ")
        user_input = int(input("Enter option : "))
        if user_input == 1:
            self.check_student()
        elif user_input == 2:
            self.assign_grade()
        elif user_input == 3:
            self.generate_report()
        elif user_input == 4:
            self.register_student()
        elif user_input == 5:
            self.register_lecturer()
        else:
            print("Enter enter correct option")   
        
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
    