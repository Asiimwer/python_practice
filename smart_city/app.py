import sqlite3
def save_to_db():
    conn = sqlite3.connect('ham_palm_city.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resident(identity_id TEXT NOT NULL,
        names TEXT NOT NULL,
        gender TEXT NOT NULL,
        address TEXT NOT NULL,
        dob TEXT NOT NULL,
        marriage_status TEXT NOT NULL,
        children TEXT,
        criminal_hsitory TEXT NOT NULL)
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workers(person_id TEXT NOT NULL,
            job TEXT NOT NULL,
            employer TEXT NOT NULL,
            education TEXT NOT NULL,
            work_history TEXT NOT NULL,
            salary TEXT NOT NULL,
            tax TEXT NOT NULL,
            FOREIGN KEY (person_id) REFERENCES resident(identity_number))
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mayor( person_id TEXT NOT NULL,
                duties TEXT NOT NULL,
                FOREIGN KEY (person_id) REFERENCES resident(identity_number))
        ''')
    cursor.execute('''
         CREATE TABLE IF NOT EXISTS admins(admin_id TEXT NOT NULL,
                   admin_password TEXT NOT NULL,
                   admin_role TEXT NOT NULL,
                   clearance_level TEXT NOT NULL)
        ''')
    conn.commit()
    conn.close()
class Person():
    def __init__(self,r_id,names,gender,dob,address):
        self.r_id = r_id
        self.names = names
        self.gender = gender
        self.dob = dob
        self.address = address
    def display_info(self):
        print(f"\n ID :{self.r_id} \n Names : {self.names} \n Gneder : {self.gender} \n DOB : {self.dob} \n Address : {self.address} ")
class Resident(Person):
    def __init__(self, r_id, names, gender, dob, address,marriage_stats,children = None,crime_hist = None):
        self.children = children
        self.crime_history = crime_hist
        self.marriage_status = marriage_stats
        self.children = children
        self.crime_hist = crime_hist
        super().__init__(r_id, names, gender, dob, address)
    def display_info(self):
        super().display_info() 
        print(f" Children : {self.children} \n Criminal History : {self.crime_history}")
    def input_resident(self):
        resident_id = input("Enter ID : ")
        names = input("Enter Names : ")
        gender = input("Enter gender : ")
        dob = input("Enter DOB : ")
        address = input("Enter address : ")
        marriage_stats = input("Enter marriage status : ")
        children = input("Enter Children : ")
        crime_hist = input("Enter criminal history : ")
        resident = Resident(resident_id,names,gender,dob,address,marriage_stats,children,crime_hist)
        conn = sqlite3.connect("ham_palm_city.db")
        cursor = conn.cursor()
        cursor.execute('''
                INSERT INTO resident(identity_id,names,gender,address,dob,marriage_status,children,criminal_hsitory)
                    VALUES(?,?,?,?,?,?,?,?) ''', (resident.r_id,resident.names,resident.gender,resident.address,resident.dob,resident.marriage_status,resident.children,resident.crime_hist))           
        conn.commit()
        conn.close()
        resident.display_info()
class Worker():
    def __init__(self, id, occupation,employer,work_history,education_history,salary,taxes):
        self.id = id
        self.occupation = occupation
        self.employer = employer
        self.education_history = education_history
        self.salary = salary
        self.taxes = taxes
        self.work_hist = work_history
    def save_worker(self) :
        resident_id = input("Input ID : ")
        occupation = input("Enter occupation : ")
        employer = input("Enter employer : ")
        edu_hist = input("Enter qualifications : ")
        salary = int(input("Enter salary : "))
        work_hist = input("Work history : ")
        taxes = 35/100
        worker =Worker(resident_id,occupation,employer,edu_hist,work_hist,salary,taxes)
        conn = sqlite3.connect("ham_palm_city.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO workers(person_id,job,employer,education,work_history,salary,tax)
                       VALUES(?,?,?,?,?,?,?) ''', (worker.id,worker.occupation,worker.employer,worker.education_history,worker.work_hist,worker.salary,worker.taxes))
        print(f"\n ID : {worker.id} \n Occupation : {worker.occupation} \n Employer : {worker.employer} \n Qualifications : {worker.education_history} \n Work History : {worker.work_hist} Salary : {worker.salary} \n Taxes : {worker.taxes} \n WOrk History : {worker.work_hist}")
        conn.commit()
        conn.close()
    def new_job(self):
        print("Admin! to workers dashboard")

class Mayor(Worker):
    def __init__(self,id,duties):
        self.id = id
        self.duties = duties
        print(f"\n Duties : {self.duties}")
    def save_mayor(self):
        resident_id = input("Enter resident_id : ")
        duties = input("Input the number of duties : ")
        mayor = Mayor(resident_id,duties)
        conn = sqlite3.connect("ham_palm_city.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO mayor(person_id,duties)
                VALUES(?,?) ''', (mayor.id,mayor.duties))
        conn.commit()
        conn.close()
        
        # ADD A WAY TO INCRESE EVERYTIME THEY PUT DUTIES
class Admin():
    def __init__(self,a_id,a_role,a_cl,a_password):
        self.a_id = a_id
        self.a_role = a_role
        self.cl = a_cl
        self.a_password = a_password
    def create_admin(self) :
        admin_id = input("Input ID : ")
        admin_role = input("Enter Admin role : ")
        clearence_level = input("Enter clearence_level : ")
        password = input("Enter password : ")
        my_admin = Admin(admin_id,admin_role,clearence_level,password)
        conn = sqlite3.connect("ham_palm_city.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO admins(admin_id,admin_role,clearance_level,admin_password)
                       VALUES(?,?,?,?) ''', (my_admin.a_id,my_admin.a_role,my_admin.cl,my_admin.a_password))
        print(f"\n ID : {my_admin. a_id} \n Role : {my_admin.a_role} \n Clearance Level : {my_admin.cl} \n Password : {my_admin.a_password}")
        conn.commit()
        conn.close()
    def admin_operator(self):
      self.admin_operator()
      if add:
          print("Admin created ")
    admin_operator()
def my_operator():
        # print("Enter '1' to check resident")
        print("Enter '1' to register Resident")
        print("Enter '2' to register Worker")
        print("Enter '3' to register Mayor")
        # print("Enter '4' to register student ")
        # print("Enter '5' to  register lecturer ")
        # print("Enter '6' to add admin")
        user_input = int(input("Enter option : "))
        if user_input == 1:
            # Why does this None thing work 
            resident = Resident(None,None,None,None,None,None,None,None)
            save = resident.input_resident()
            if save:
                print("Woker saved")
        elif user_input == 2:
             worker = Worker(None,None,None,None,None,None,None)
             worker.save_worker()
        elif user_input == 3:
           mayor = Mayor(None,None)
           save = mayor.save_mayor()
           if mayor:
               print("Mayor saved")
        else:
            print("Wrong Input") 




if __name__ == "__main__":
    save_to_db()