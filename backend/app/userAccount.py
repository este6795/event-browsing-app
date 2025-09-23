"""
userAccount.py
User account management for an event browsing app
Developed by Alex and Dean


Requirements: 
- Creating a user account with a unique username and password
- Creating login in functionality
- Password change/recovery 
- Verifying emails are valid
- Deleting user accounts 
- Identifying and handling database related areas 
"""
import sqlite3, re, hashlib

DB_NAME = "EventPlannerDB.db"
class User:
    """
    User account management for the event browsing app.
    
    This class manages user sign up, login, password recovery, profile updates, and account deletion.
    Users are stored in a multidimensional dictionary, where each username maps to a dictionary containing their password and email.
    """
    def __init__(self, username:str, password:str, email=None):
        """
        Initialize a User object.
        Args:
            username (str): The username for this user instance.
            password (str): The password for this user instance.
            email (str, optional): The email for this user instance.
        """
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        """
        Returns a string representation of the User object.
        """
        return f"User(username={self.username}, password={self.password} ,email={self.email})"

    @staticmethod
    def init_db():
        """
        A method that initializes the database and creates the accounts table if it doesn't exist.
        """
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE accounts (
            BearID INTEGER PRIMARY KEY, 
            username VARCHAR(20), 
            password VARCHAR (50), 
            recoveryEmail VARCHAR(60),     
            RSVPEvents MEDIUMBLOB,             
            LikedEvents MEDIUMBLOB,
            CreatedEvents MEDIUMBLOB,

            FOREIGN KEY (eventID) REFERNCES events

            ;)""")
        conn.commit()
        conn.close()       

    @staticmethod
    def connect():
        """
        Connect to the SQLite database and return the connection object.
        """
        return sqlite3.connect(DB_NAME)

    @staticmethod
    def valid_email(email):
        """
        Validate the email format using a regular expression.
        Returns True if the email is valid, False otherwise.
        """
        if email is None:
            return False
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @classmethod
    def sign_up(cls, username, password, email=None):
        """
        Sign up a new user.
        Takes a username, password, and optionally an email. Checks if the username is unique and if the password is long enough (at least 13 characters).
        Adds the user to the users dictionary if valid.
        Returns a success message or raises ValueError if checks fail.
        """
        conn = cls.connect()
        cursor = conn.cursor()

        # Password and email validation
        if len(password) <= 12:
            raise ValueError("Password must be at least 12 characters long")
        if not cls.valid_email(email):
            raise ValueError("Invalid email format")
        
        # Check for unique username in the database
        cursor.execute("SELECT 1 FROM accounts WHERE username = ?", (username,))
        if cursor.fetchone():
            raise ValueError("Username already exists, please choose another")
        
        # Insert new user into the database
        cursor.execute(
            "INSERT INTO accounts (username, password, recoveryEmail) VALUES (?, ?, ?)", 
                       (username, password, email),
                       )
        conn.commit()
        conn.close()
        
    @classmethod
    def log_in(cls, username, password):
        """
        Log in a user.
        Checks if the username and password match an entry in the accounts database.
        Returns a success message or raises ValueError if credentials are invalid.
        """
        conn = cls.connect()
        cursor = conn.cursor()

        #Find the account in the database
        cursor.execute("SELECT * FROM accounts WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        #If the user exists, return success message
        if user:
            return "Login successful"
        else:
            raise ValueError("Invalid username or password")
        
    @classmethod
    def password_recovery(cls, username, new_password, email=None):
        """
        Checks if user exists in the database with matching username and email.
        If so, updates the password to the new password provided.
        """
        # Password and email validation
        if len(new_password) <= 12:
            raise ValueError("Password must be at least 12 characters long")
        if not cls.valid_email(email):
            raise ValueError("Invalid email format")
        
        conn = cls.connect()
        cursor = conn.cursor()

        #Update the password for the user if username and email match
        cursor.execute("UPDATE accounts SET password = ? WHERE username = ? AND recoveryEmail = ?", (new_password, username, email))
        cursor.commit()
        update = cursor.rowcount
        conn.close()

        if update:
            return "Password updated successfully"
        else:
            raise ValueError("Username and email do not match any account")

    def update_profile(self, new_email=None, new_password=None):
        """
        Update the profile of the current user instance.
        Allows changing the email and/or password for this user object as well as database.
        """
        conn = self.connect()
        cursor = conn.cursor()
        
        # Email validation and database update
        if new_email:
            if not self.valid_email(new_email):
                raise ValueError("Invalid email format")
            cursor.execute("UPDATE accounts SET recoveryEmail = ? WHERE username = ?", (new_email, self.username))
            self.email = new_email

        # Password validation and database update
        if new_password:
            if len(new_password) <= 12:
                raise ValueError("Password must be at least 12 characters long")
            cursor.execute("UPDATE accounts SET password = ? WHERE username = ?", (new_password, self.username))
            self.password = new_password
        
        conn.commit()
        conn.close()
                
    @classmethod
    def delete_account(cls, username, password, email=None):
        """
        Delete a user account from the account database.
        Checks if the username, password, and email match, then removes the user.
        Returns a success message if deleted.
        """
        conn = cls.connect()
        cursor = conn.cursor()

        # Delete the user if username, password, and email match
        cursor.execute("DELETE FROM accounts WHERE username = ? AND password = ? AND recoveryEmail = ?", (username, password, email))
        conn.commit()
        deleted = cursor.rowcount
        conn.close()

        if deleted:
            return "Account deleted successfully"
        else:
            raise ValueError("Username, password, and email do not match any account")
        
