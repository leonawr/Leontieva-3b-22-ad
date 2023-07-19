import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students
(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, average_score REAL)''')

students_data = [('Вася', 19, 4.7),
                 ('Петя', 21, 5.0),
                 ('Вова', 24, 3.2)]

cursor.executemany("INSERT INTO students (name, age, average_score) VALUES (?, ?, ?)", students_data)
conn.commit()
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(f'Name: {row[1]}, Age: {row[2]}, Average Score: {row[3]}')

conn.close()