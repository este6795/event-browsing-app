# Code meant for user account management

class User: 
    def __init__(self, username, password, email=None):
        self.username = username
        self.password = password
        self.email = email
        self.users = {"Alex" : {"password": "password123", "email": None}}

    def __repr__(self):
        return f"User(username={self.username}, password={self.password} ,email={self.email})"

    def sign_up(self, username, password, email=None):
        # Logic for signing up a user
        for user in self.users:
            if user == username:
                raise ValueError("Username already exists")
            else: 
                if len(password) <= 12: 
                    raise ValueError("Password must be at least 12 characters long")
                else: 
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




# Testing 
print("Hello welcome please sign up or log in")

test_user = User(username="testuser", password="securepassword123", email="test@example.com")
assert test_user.username == "testuser", "Username not set correctly"
assert test_user.password == "securepassword123", "Password not set correctly"
assert test_user.email == "test@example.com", "Email not set correctly"
print("User creation test passed.")