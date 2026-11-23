import sqlite3

conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.executescript("""
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS movies;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER CHECK(rating >= 1 AND rating <= 10),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);
""")

users = [("Алиса",), ("Боб",), ("Чарли",), ("Диана",), ("Ева",)]
cursor.executemany("INSERT INTO users (name) VALUES (?);", users)

movies = [
    ("Начало", "Фантастика"),
    ("Темный рыцарь", "Боевик"),
    ("Интерстеллар", "Фантастика"),
    ("Паразиты", "Триллер"),
    ("Неизвестный шедевр", "Драма"),
]
cursor.executemany("INSERT INTO movies (title, genre) VALUES (?, ?);", movies)

reviews = [
    (1, 1, 9), (2, 1, 10), (3, 1, 8),
    (1, 2, 10), (4, 2, 9), (5, 2, 10),
    (2, 3, 9), (3, 3, 7),
    (4, 4, 8), (5, 4, 9), (1, 4, 8)
]
cursor.executemany("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?);", reviews)
conn.commit()

cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id;
""")
for row in cursor.fetchall():
    print(row)

cursor.execute("""
SELECT movies.title, movies.genre, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id;
""")
for row in cursor.fetchall():
    print(row)

cursor.execute("""
SELECT ROUND(AVG(rating), 2), MAX(rating), MIN(rating)
FROM reviews;
""")
print(cursor.fetchone())

conn.close()
