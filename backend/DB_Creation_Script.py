import sqlite3

sqliteConnection = sqlite3.connect("EventPlannerDB.db")
cursor = sqliteConnection.cursor()

#This script is just for making the table, logic like email authentication will be elsewhere
#I was hoping to do the RSVPEvents and LikedEvents as a list, all I could find is BLOB, and 
#idk how they work yet (growth mindset)
#but we might just end up needing to treat it like a CSV and cry about it

sql_command = """CREATE TABLE accounts (
BearID INTEGER PRIMARY KEY, 
username VARCHAR(20), 
password VARCHAR (50), 
recoveryEmail VARCHAR(60),     
RSVPEvents MEDIUMBLOB,             
LikedEvents MEDIUMBLOB,

CreatedEvents MEDIUMBLOB,

FOREIGN KEY (eventID) REFERNCES events

;)"""       

cursor.execute(sql_command)


sql_command = """CREATE TABLE events (
eventID INTEGER PRIMARY KEY AUTO_INCREMENT,     
FOREIGN KEY (BearID) REFERENCES accounts, 
eventName VARCHAR(50) NOT NULL, 
eventDescription VARCHAR(250) NOT NULL,         
images MEDIUMBLOB,                                        
eventType SET ("Sports","Honors", "Workshops", "Study Session"),    
eventAccess ENUM ("Public", "Private"), 
startDateTime DATETIME NOT NULL, 
endDateTime DATETIME NOT NULL, 
listOfUsersRSVPd MEDIUMBLOB, 
numberOfLikes INTEGER(6),       
listOfUsersLiked MEDIUMBLOB;)"""

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

cursor.execute(sql_command)
sqliteConnection.close()