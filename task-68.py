import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies
(id INTEGER PRIMARY KEY, name TEXT, genre TEXT, rating REAL)''')

movies_data = [('Унесённые призраками', 'аниме', 8.5),
              ('Зеленая миля', 'драма', 9.1),
              ('Интерстеллар', 'фантастика', 8.6)]

cursor.executemany("INSERT INTO movies (name, genre, rating) VALUES (?, ?, ?)", movies_data)

conn.commit()

cursor.execute('SELECT * FROM movies WHERE genre = "драма"')
rows = cursor.fetchall()

for row in rows:
    print(f'Name: {row[1]}, genre: {row[2]}, rating: {row[3]}')

conn.close()