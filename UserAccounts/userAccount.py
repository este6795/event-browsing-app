#import SQLalchemy

# NEED TO ASK HOW MUCH OF THIS LOGIC IS ALREADY GOING TO BE HANDLED BY THE FRONT END
class userAccount:
    def __init__(self, user = None, userPass, email):
        #username = verifyUsernameUnique(user)
        
        password = userPass
        # add password to DB
        

        #VERIFY EMAIL IS REAL
        #recoveryEmail = verifyEmailValid(email)
        # add email to DB
        pass

    def verifyUsernameUnique(self, username):
        # VERIFY USERNAME IS UNIQUE
        # user inputs their email
        # call to database to check uniqueness
        # while loop until they submit a valid one
        
        return
    
    def verifyEmailValid(self, email):
        #while loop until they submit a valid email
        pass

    def changePass(self, newPass):
        #assuming that it has already been verified that this is a valid password change
        self.password = newPass

    def changeEmail(self, newEmail):
        self.email = verifyEmailValid(newEmail)


    def getEncryptedPassHash(self):
        #used when logging in, to check user input password attempt against the stored password
        pass

    def attemptingLogin(self):
        #for loop, only given three tries to submit a valid password

        pass

    def deleteAccount(self):
        pass