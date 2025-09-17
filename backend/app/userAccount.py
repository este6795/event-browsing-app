
# userAccount.py
# User account management for an event browsing app
# Developed by Alex and Dean


class User:
    """
    User account management for the event browsing app.
    
    This class manages user sign up, login, password recovery, profile updates, and account deletion.
    Users are stored in a multidimensional dictionary, where each username maps to a dictionary containing their password and email.
    """
    def __init__(self, username, password, email=None):
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
        self.users = {}

    def __repr__(self):
        return f"User(username={self.username}, password={self.password} ,email={self.email})"

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
   
    def password_recovery(self, username, password, email=None):
        # Logic for password recovery
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
   
    def delete_account(self, username, password, email=None):
        """
        Delete a user account from the users dictionary.
        Checks if the username, password, and email match, then removes the user.
        Returns a success message if deleted.
        """
        if username in self.users and self.users[username]["password"] == password and self.users[username]["email"] == email:
            del self.users[username]
            return "Account deleted successfully"
