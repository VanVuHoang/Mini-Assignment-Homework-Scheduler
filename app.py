from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = "data.db"

app = Flask(__name__)

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as err:
        print(err)
    return None

def fetchall(db_file, query):
    con = create_connection(db_file)
    cur = con.cursor()
    cur.execute(query)
    allfetched = cur.fetchall()
    con.commit()
    con.close()
    return allfetched

@app.route('/')
def render_menu_page():
    students_list = fetchall(DATABASE, f'SELECT id, name, homework_id FROM student')
    homeworks_list = fetchall(DATABASE, f'SELECT subject FROM homework')
    homeworks = []
    for homework in homeworks_list:
        homeworks.append(homework[0])
    return render_template('app.html', students=students_list, homeworks=homeworks)


app.run(host='0.0.0.0', debug=True)