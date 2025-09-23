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
import sqlite3, re

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
    def connect_db():
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
    def sign_up(self, username, password, email=None):
        """
        Sign up a new user.
        Takes a username, password, and optionally an email. Checks if the username is unique and if the password is long enough (at least 13 characters).
        Adds the user to the users dictionary if valid.
        Returns a success message or raises ValueError if checks fail.
        """
        if username in self.users:
            raise ValueError("Username already exists")
        if len(password) <= 12:
            raise ValueError("Password must be at least 12 characters long")
        self.users[username] = {"password": password, "email": email}
        return "User signed up successfully"
    
    @classmethod
    def log_in(self, username, password):
        """
        Log in a user.
        Checks if the username and password match an entry in the users dictionary.
        Returns a success message or raises ValueError if credentials are invalid.
        """
        if username in self.users and self.users[username]["password"] == password:
            return "Login successful"
        else:
            raise ValueError("Invalid username or password, please try again")
   
    @classmethod
    def password_recovery(self, username, password, email=None):
        """
        Checks if user exists and updates their password.
        """
        for user in self.users:
            if user.username == username and user.email == email:
                user.password = password
                return "Password updated successfully"
            else:
                raise ValueError("Invalid username or email")
        
    def update_profile(self, new_email=None, new_password=None):
        """
        Update the profile of the current user instance.
        Allows changing the email and/or password for this user object (not the users dictionary).
        """
        if new_email:
            self.email = new_email
        if new_password:
            self.password = new_password
   
    @classmethod
    def delete_account(self, username, password, email=None):
        """
        Delete a user account from the users dictionary.
        Checks if the username, password, and email match, then removes the user.
        Returns a success message if deleted.
        """
        if username in self.users and self.users[username]["password"] == password and self.users[username]["email"] == email:
            del self.users[username]
            return "Account deleted successfully"
