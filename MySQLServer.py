import mysql.connector

mydb = mysql.connector.connect(
     host = "localhost",
    user="root",
    passwd="SIbro@124"
    # database="testdatabase"
)

myCursor = mydb.cursor()

myCursor.execute("""CREATE DATABASE IF NOT EXISTS alx_book_store""")

print("Database 'alx_book_store' created successfully!")

myCursor.close()
mydb.close()