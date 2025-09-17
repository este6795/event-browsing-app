# Code meant for user account management

class User: 
    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email
        self.users = {}

    def __repr__(self):
        return f"User(username={self.username}, password={self.password} ,email={self.email})"

    def sign_up(self, username, password, email=None):
        # Logic for signing up a user
        if username in self.users:
            raise ValueError("Username already exists")
        if len(password) <= 12:
            raise ValueError("Password must be at least 12 characters long")
        self.users[username] = {"password": password, "email": email}
        return "User signed up successfully"
    
    def log_in(self, username, password):
        # Logic for logging in a user
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
        # Logic for updating user profile
        if new_email:
            self.email = new_email
        if new_password:
            self.password = new_password
   
    def delete_account(self, username, password, email=None):
        # Logic for deleting a user account
        if username in self.users and self.users[username]["password"] == password and self.users[username]["email"] == email:
            del self.users[username]
            return "Account deleted successfully"
