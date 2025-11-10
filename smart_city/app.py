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
        print(f"\n ID :{self.id} \n Names : {self.names} \n Gneder : {self.gender} \n DOB : {self.dob} \n Address : {self.address} ")
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
        print(f"\n Children : {self.children} \n Criminal History : {self.crime_history}")
    def input_resident(cls):
        resident_id = input("Enter ID : ")
        names = input("Enter Names : ")
        gender = input("Enter gender : ")
        dob = input("Enter DOB : ")
        address = input("Enter address : ")
        marriage_stats = input("Enter marriage status : ")
        children = input("Enter Children : ")
        crime_hist = input("Enter criminal history : ")
        resident = cls(resident_id,names,gender,dob,address,marriage_stats,children,crime_hist)
        conn = sqlite3.connect("ham_palm_city.db")
        cursor = conn.cursor()
        cursor.execute(''''
                INSERT INTO resident(identity_id,names,gender,address,dob,marriage_status,children,criminal_history)
                    VALUES(?,?,?,?,?,?,?,?) ''', (self.r_id,self.names,self.gender,self.address,self.dob,self.marriage_status,self.children,self.crime_hist))
        conn.commit()
        conn.close()
        resident.display_info()
class Worker():
    def __init__(self, id, occupation,employer,education_history,salary,taxes):
        self.id = id
        self.occupation = occupation
        self.employer = employer
        self.education_history = education_history
        self.salary = salary
        self.taxes = taxes
    def display_info(self) :
        print(f"\n ID : {self.id} \n Occupation : {self.occupation} \n Employer : {self.employer} \n Salary : {self.salary} \n Taxes : {self.taxes}")
        resident_id = input("Input ID : ")
        occupation = input("Enter occupation : ")
        employer = input("Enter employer : ")
        edu_hist = input("Enter qualifications : ")
        salary = int(input("Enter salary : "))
        taxes = 35/100*salary
        worker=Worker(resident_id,occupation,employer,edu_hist,salary,taxes)
        conn = sqlite3.connect("ham_palm_city.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO worker(person_id,job,employer,education,work_history,salary,tax)
                       VALUES(?,?,?,?,?,?,?) ''', (self.id,self.occupation,self.employer,self.education_history,self.salary,self.taxes))
        conn.commit()
        conn.close()
        worker.display_info()
class Mayor():
    def __init__(self,id,duties):
        self.id = id
        self.duties = duties
        print(f"\n Duties : {self.duties}")
    def save_mayor(self):
        resident_id = input("Enter resident_id : ")
        duties = input("Input the number of duties : ")
        Mayor(resident_id,duties)
        conn = sqlite3.connect("ham_palm_city.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO mayor(person_id,duties)
                VALUES(?,?) ''', (self.id,self.duties))
        conn.commit()
        conn.close()
        # ADD A WAY TO INCRESE EVERYTIME THEY PUT DUTIES

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
            resident = Resident()
            resident.input_resident()
        elif user_input == 2:
             Worker.save_worker
        elif user_input == 3:
           Mayor.save_mayor()
        else:
            print("Wrong Input") 
my_operator()      
if __name__ == "__main__":
    save_to_db()