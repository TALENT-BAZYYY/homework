import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER
    )
''')
conn.commit()


def create_book(title, author, year):
    cursor.execute(
        'INSERT INTO books (title, author, year) VALUES (?, ?, ?)',
        (title, author, year)
    )
    conn.commit()


def read_books():
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    for book in books:
        print(book)


def update_book(book_id, new_year):
    cursor.execute(
        'UPDATE books SET year = ? WHERE id = ?',
        (new_year, book_id)
    )
    conn.commit()


def delete_book(book_id):
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()


create_book('Белый пароход', 'Чингиз Айтматов', 1970)
create_book('Преступление и наказание', 'Федор Достоевский', 1866)
create_book('1984', 'Джордж Оруэлл', 1948)

read_books()

update_book(3, 1949)
read_books()

delete_book(2)
read_books()

conn.close()
