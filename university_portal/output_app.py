from flask import Flask, render_template
import sqlite3

def home_page():
    conn = sqlite3.connect('student_portal')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    all_data = cursor.fetchall()
    conn.commit()
    conn.close()
    return render_template('index.html',all_data=all_data)