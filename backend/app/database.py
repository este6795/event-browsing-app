import sqlite3

# connecting to the database
connection = sqlite3.connect("gfg.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE userData ( 
userID INTEGER PRIMARY KEY, 
username VARCHAR(20), 
password CHAR(1), 
joining DATE);"""

# execute the statement
crsr.execute(sql_command)

# close the connection
connection.close()