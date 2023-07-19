import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS book
(id INTEGER PRIMARY KEY, name TEXT, author TEXT, year INTEGER)''')

books_data = [('О дивный новый мир', 'Олдос Хаксли', 1932),
              ('Парфюмер', 'Патрик Зюскинд', 1985),
              ('Гарри Поттер и Орден Феникса', 'Джоан Кэтрин Роулинг', 2003)]

cursor.executemany("INSERT INTO books (name, author, year) VALUES (?, ?, ?)", books_data)
conn.commit()
cursor.execute('SELECT * FROM books WHERE year > 2000')
rows = cursor.fetchall()

for row in rows:
    print(f'Name: {row[1]}, author: {row[2]}, author: {row[3]}')
conn.close()