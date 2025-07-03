import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd="SIbro@124",
    database="testdatabase"
)

print(db.get_server_info())
print("----------")
mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE testdatabase")

mycursor.execute("SHOW DATABASES")
for database in mycursor:
    print(database)
# print('connected')

mycursor.execute("""
                 CREATE TABLE IF NOT EXISTS students (
                 id INT AUTO_INCREMENT PRIMARY KEY,
                 name VARCHAR(200),
                 age INT
                 )
                 """)

# create data in table
# sql = "INSERT INTO students (name, age) VALUES(%s, %s)"
# val = ("Topzee", 21)
# mycursor.execute(sql, val)
# db.commit() #note this, don't forget
# print("1 record inserted")

# read data from db table
mycursor.execute("SELECT *  FROM students")
results = mycursor.fetchall()

for row in results:
    print(row)

# update data

sql = "UPDATE students SET age = %s WHERE name = %s"
val = (22, "Topzee" )
mycursor.execute(sql, val)
db.commit()
print("Record Updated.")

# Delete item
sql = "DELETE FROM students WHERE id = %s"
val = (3,)
mycursor.execute(sql, val)
db.commit()
print("Delete successful")

# Close connection to the databasse 
mycursor.close()
db.close()