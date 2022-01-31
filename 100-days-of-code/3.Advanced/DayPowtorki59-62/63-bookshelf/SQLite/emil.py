import sqlite3

db = sqlite3.connect("book.db")

cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE,author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
cursor.execute("INSERT INTO books VALUES (1, 'Ksiazka','Autor Nieznany', '9.3')")
db.commit()