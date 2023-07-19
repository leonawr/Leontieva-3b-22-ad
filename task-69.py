import sqlite3

conn = sqlite3.connect('employees.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
(id INTEGER PRIMARY KEY, name TEXT, position INTEGER, wage INTEGER)''')

employees_data = [('Аня', 'manager', 100000),
                  ('Катя', 'manager', 90000),
                  ('Вероника', 'data analyst', 200000)]

cursor.executemany("INSERT INTO employees (name, position, wage) VALUES (?, ?, ?)", employees_data)
conn.commit()
cursor.execute('SELECT * FROM employees WHERE position = "manager"')
rows = cursor.fetchall()

for row in rows:
    print(f'Name: {row[1]}, genre: {row[2]}, rating: {row[3]}')

conn.close()