"""
Database setup script for user information management:

Name of Database: "EventPlannerDB.db"


Tables in Database:
accounts (BearID (primary key), username, password, recoveryEmail, RSVPEvents, LikedEvents)

Note: 
- recovery email should probably be authenticated (or just checked for syntax) to be a bears.unco.edu or a first.last@unco.edu email
- usernames must be moderated to prevent offensive names
- passwords should be hashed and salted for security


Events (eventID (primary Key), eventName, eventDescription, images, eventType, 
               eventAccess (aka public or private), startDateTime, endDateTime, 
               listOfUsersRSVPd, numberOfLikes, listOfUsersLiked)

Use https://sqlitebrowser.org/ to view structures of databases and their contents
"""

import sqlite3

# connecting to the database
connection = sqlite3.connect("gfg.db")

# cursor
crsr = connection.cursor()

# print statement will execute if there
# are no errors
print("Connected to the database")

# close the connection
connection.close()