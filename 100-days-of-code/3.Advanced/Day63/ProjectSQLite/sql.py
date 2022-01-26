import sqlite3

#connection to a new database(if the database does not exist then it will be created)
db = sqlite3.connect("book-collection.db")

# Create a cursor which will control our database(this is the mouse pointer)
cursor = db.cursor()

#Create tables
#execute() - this method will tell the cursor to execute an action
#create table - create a new table in the database
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K.Rowling', '9.3')")
db.commit()