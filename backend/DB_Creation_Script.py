import sqlite3

sqliteConnection = sqlite3.connect("EventPlannerDB.db")
cursor = sqliteConnection.cursor()

#========================================================================================
# SqlLite  methods
# to create a query, create a multiline string with """  args """
# 



#=========================================================================================
#This script is just for making the table, logic like email authentication will be elsewhere
#I was hoping to do the RSVPEvents and LikedEvents as a list, all I could find is BLOB, and 
#idk how they work yet (growth mindset)
#but we might just end up needing to treat it like a CSV and cry about it

sql_command = """CREATE TABLE accounts (
accountID INTEGER PRIMARY KEY AUTO_INCREMENT, 
username VARCHAR(20) UNIQUE,
accountType ENUM ("Student", "Faculty")
password VARCHAR (50), 
recoveryEmail VARCHAR(60),     
RSVPEvents MEDIUMBLOB,             
LikedEvents INTEGER (5),
CreatedEvents MEDIUMBLOB;)"""

cursor.execute(sql_command)






# OPTION A)  This is a Log of RSVPs, which references both Event ID and 
#            ?? Create logic to delete all rsvps of an event once the event is over?
#                     ?? should we create logic to delete an event automatically 24-72 hours after its endDateTime?
#            PRIMARY KEY is (eventID, userWhoRSVPID), there is no singular candidate key
sql_command = """ CREATE TABLE RSVPed_Events ( 
eventID INTEGER (10) NOT NULL,
creatorID (10) NOT NULL,
userWhoRSVPID (10) NOT NULL,

FOREIGN KEY (eventID) REFERENCES events,
FOREIGN KEY (creatorID) REFERENCES events(accountID),
FOREIGN KEY (userWhoRSVPID) REFERENCES accounts(accountID);
)"""
cursor.execute(sql_command)





sql_command = """CREATE TABLE events (
eventID INTEGER PRIMARY KEY AUTO_INCREMENT,     
accountID INTEGER (10), 
accountType ENUM 
eventName VARCHAR(50) NOT NULL, 
eventDescription VARCHAR(250) NOT NULL,         
images MEDIUMBLOB,                                        
eventType SET ("Sports","Honors", "Workshops", "Study Session"),    
eventAccess ENUM ("Public", "Private"), 
startDateTime DATETIME NOT NULL, 
endDateTime DATETIME NOT NULL, 
listOfUsersRSVPd MEDIUMBLOB, 
numberOfLikes INTEGER(5),

FOREIGN KEY (accountID) REFERENCES accounts,
FOREIGN KEY (accountType) REFERENCES accounts
)"""



cursor.execute(sql_command)



#("Sports","Honors", "Workshops", "Study Session", "Dissertation", "Performance", "Competition", "", "", "", "", "", "", "")
# Event Types - ("")
# departments - ("Art", "Math", "Science", "Computer Science", "History", "Education", "Political Science", "Software Engineering", "Business")


#I'm not sure if/how the AUTO_INC on eventID changes how we input data into the db 
#eventDescription is only 250 characters, could increase if desired

#I'm using mediumblobs because they don't require that I insert a size, as idk what that means
#eventually will switch this back to BLOB(arg), once I understand them better
    #I'm not sure how to do Images, but I think BLOBs will work


#Event Types could be expanded on further, could include each college, each department, 
#Pulling from UNC's list of events, could also reasonably include: 
# "Competition", "Video Games", "Dissertation Defense", "Astronomy"
# I think we should plan for types to be combined, so the 3v3 BBall tourny would be "Sports", "Competition"
# The SET data type allows 0 or more from selected type

#I think numberofLikes INTEGER(6) means that val has 6 digits, could be wrong


sqliteConnection.commit()
sqliteConnection.close()