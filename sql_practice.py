import mysql.connector

mydb = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    passwd='SIbro@124',
    database='books'
)

myCursor = mydb.cursor()

# myCursor.execute("CREATE DATABASE books")

myCursor.execute("SHOW DATABASES")
myCursor.fetchall() # can also use this to fetch all db
# for database in myCursor:
#     print(database)

myCursor.execute("""CREATE TABLE IF NOT EXISTS books(
                 id INT AUTO_INCREMENT PRIMARY KEY,
                 title VARCHAR(255),
                 author VARCHAR(255),
                 ISBN VARCHAR(255)
                 )
                 """)

# INSERT BOOK DETAILS
# sql = """INSERT INTO books (title, author, ISBN) VALUES(%s, %s, %s)"""
# vals= [
#         ('Automate the Boring Stuff with Python', 'Luciano Ramalho', '9781491946008'),
#         ('Fluent Python', 'Luciano Ramalho', '9781491046008'),
#         ('Python Crash Course', 'Eric Matthes', '9781593279288'),
#         ('Learning SQL', 'Alan Beaulieu', '9780596520830'),
#         ('SQL in 10 Minutes, Sams Teach Yourself', 'Ben Forta', '9780672336072')
#         ]
# myCursor.executemany(sql, vals)
# mydb.commit()

# print(f"{myCursor.rowcount} records inserted")

# search books by title
title_input = input("Enter the book you're looking for: ")
myCursor.execute("SELECT * FROM books WHERE title = %s", (title_input,))
result = myCursor.fetchall()
# print details of searched book
if result:
    print("\n Search Result: ")
    for row in result:
        print(row)
else:
    print("Book not found")
# print(result)

# list all books
myCursor.execute("SELECT * FROM books")
results = myCursor.fetchall()

print("\n All Books")
for row in results:
    print(row)

# bonus challenge, delete a book
sql = "DELETE FROM books WHERE id = %s"
id = 4
val = (id,)
myCursor.execute(sql, val)
mydb.commit()
print(f"successfully deleted id: {id}" )

# list all books
myCursor.execute("SELECT * FROM books")
results = myCursor.fetchall()

print("\n All Books")
for row in results:
    print(row)

# close connection
myCursor.close()
mydb.close()