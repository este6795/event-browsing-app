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

# close the connection
connection.close()