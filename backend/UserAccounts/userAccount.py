import sqlite3
import re

sqliteConnection = sqlite3.connet('EventPlannerDB.db')
cursor = sqliteConnection.cursor()

# NEED TO ASK HOW MUCH OF THIS LOGIC IS ALREADY GOING TO BE HANDLED BY THE FRONT END
class userAccount:
    def __init__(self, user = None, userPass, email):
        sql_command = """INSERT INTO accounts VALUES () """
        #username = verifyUsernameUnique(user)
        

        password = userPass
        # add password to DB
        
        
        #VERIFY EMAIL IS REAL
        #recoveryEmail = verifyEmailValid(email)
        # add email to DB
        cursor.execute(sql_command)
        sqliteConnection.commit()

    def getAccountBearID(self):


        return


    def verifyUsernameUnique(self, username):
        # VERIFY USERNAME IS UNIQUE
        # user inputs their email
        # call to database to check uniqueness
        # while loop until they submit a valid one
        
        return
    
    def verifyEmailValid(self, email):
        #while loop until they submit a valid email

        #OPTION A) run through a regex to that it has a valid format for a unco email




        #OPTION B) send a verification email (dont think this is feasible, I think this needs a server to recieve the verification, and idk how to)

        pass

    def changePass(self, newPass):
        #assuming that it has already been verified that this is a valid password change
        userID = getAccountBearID()

        sql_command = """
        UPDATE
        SET
        WHERE 
        """



        cursor.execute(sql_command)
        sqliteConnection.commit()

    def changeEmail(self, newEmail):
        self.email = verifyEmailValid(newEmail)
        sqliteConnection.commit()


    def getEncryptedPassHash(self):
        #used when logging in, to check user input password attempt against the stored password
        pass

    def attemptingLogin(self):
        #for loop, only given three tries to submit a valid password

        pass

    def deleteAccount(self):
        pass

sqliteConnection.close()