"""
Database Basics: 
- import sqlite3 to import library
- sqliteConnection = sqlite3.connect('filename.db')  Establishing a connection, variable can be any name
- cursor = sqliteConnection.cursor()  Creating a cursor object using the cursor() method, variable can be any name
     - cursor is used to execute SQL commands
     - You must first create a variable that contains the command, then call cursor.execute(variable) to execute it
          - Alternatively, you can call cursor.execute("SQL COMMAND") directly 
     - sqliteConnection.commit()  Saves your changes in the database
     - Use .fetchall() to get all the data from a table
     - To modify data use UPDATE table_name SET column1 = value1, column2 = value2,…  WHERE condition;
     - To delete data use DELETE FROM table_name WHERE condition;
     - To delete a table use DROP TABLE table_name;
"""
import sqlite3

# connecting to the database
connection = sqlite3.connect("userInfo.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE userData ( 
userID INTEGER PRIMARY KEY, 
username VARCHAR(50), 
password VARCHAR(50), 
joining DATE);"""

# execute the statement
crsr.execute(sql_command)

# another SQL command to insert the data in the table
sql_command = """INSERT INTO userData VALUES (23455008075532, "testUser","password123", "9/18/2025");"""
crsr.execute(sql_command)

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()

# execute the command to fetch all the data from the table emp
crsr.execute("SELECT * FROM userData")

# store all the fetched data in the ans variable
ans = crsr.fetchall()

# Since we have already selected all the data entries
# using the "SELECT *" SQL command and stored them in
# the ans variable, all we need to do now is to print
# out the ans variable
for i in ans:
    print(i)

"""
# Delete the table
crsr.execute('''DROP TABLE Student;''')

# Commit your changes in the database
connection.commit()
"""

# close the connection
connection.close()