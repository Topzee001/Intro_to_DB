import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user="root",
        passwd="SIbro@124"
        # database="testdatabase"
    )

    myCursor = mydb.cursor()

    myCursor.execute("""CREATE DATABASE IF NOT EXISTS alx_book_store""")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'myCursor' in locals() and myCursor:
        myCursor.close()
    if 'mydb' in locals() and mydb:
        mydb.close()



