import mysql.connection as mysql

try:
   db = mysql.connector.connect(
   host="",
   user="root",
   password="root")
   print("Connected succesfully")
except mysql.Error as e:
    print(e)
    print("Failed to connect")

try:
    command_handler = db.cursor()
    command_handler.execute("CREATE DATABASE testdb")
    print("testdb has been created successfully")
    
except mysql.Error as e:
    print("Could not create database")
    print(e)

#View databaes
try:
    command_handler.execute("SHOW DATABASES")
    print("these are the available databases")
    for database in command_handler:
        print(database)
except Exception as e:
    print("Could not show all databases")
    print(e)

#Connecting to an existing database
try:
    db1 = mysql.connect(host=host,user=user,password=password,database="College_db")
    print("Connected to collegedb")
except Exception as e:
    print("Failed to connect to the database")
    print(e)

#Creating tables in a database
try:
    command_handler = db1.cursor()
    command_handler.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), engine_size VARCHAR(255))")
    print("Table created successfully")
except Exception as e:
    print("Table could not be created")
    print(e)

#Showing tables in the db selected
command_handler.execute("SHOW TABLES")
print("Showing all tables in the database")
for table in command_handler:
    print(table)

#Adding data into the table
query = "INSERT INTO users(name,engine_size) VALUES(%s,%s)"
query_vals = ("Focus", "1.8L")
command_handler.execute(query, query_vals)
db1.commit()
print(command_handler.rowcount, "record inserted")