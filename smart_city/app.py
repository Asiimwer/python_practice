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
        criminal hsitory TEXT NOT NULL)
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

if __name__ == "__main__":
    save_to_db()