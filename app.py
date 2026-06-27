from flask import Flask, render_template, request, redirect
import mysql.connector
import time

app = Flask(__name__)

connected = False

while not connected:
    try:
        db = mysql.connector.connect(
            host="mysql-service",
            user="root",
            password="root",
            database="todo_db"
        )

        connected = True

    except:
        print("Waiting for MySQL...")
        time.sleep(5)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255)
)
""")

db.commit()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']

    cursor.execute(
        "INSERT INTO tasks (task) VALUES (%s)",
        (task,)
    )

    db.commit()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    cursor.execute(
        "DELETE FROM tasks WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
