from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

def get_user():
    conn = sqlite3.connect("student_portal.db")
    conn.row_factory= sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT student_no,student_name,student_gender FROM student ")
    student = cursor.fetchall()
    conn.close()
    return student

@app.route('/')
def flask_route():
    student_data = get_user()
    return render_template("index.html",student_info = student_data )

if __name__ == "__main__":
        app.run(debug=True)
