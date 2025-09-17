"""
Test created using Github Copilot!!!!
Prompt: Write unit tests for the userAccount.py file using unittest framework.

To use please run: python3 -m unittest tests/test_userAccount.py
"""

import unittest
from app.userAccount import User

class TestUserAccount(unittest.TestCase):
    def setUp(self):
        self.user = User(username="testuser", password="securepassword123", email="test@example.com")

    def test_sign_up_success(self):
        result = self.user.sign_up("newuser", "longpassword1234", "new@example.com")
        self.assertEqual(result, "User signed up successfully")
        self.assertIn("newuser", self.user.users)

    def test_sign_up_existing_username(self):
        with self.assertRaises(ValueError):
            self.user.sign_up("Alex", "anotherpassword1234")

    def test_sign_up_short_password(self):
        with self.assertRaises(ValueError):
            self.user.sign_up("shortuser", "shortpwd")

    def test_log_in_success(self):
        self.user.sign_up("loginuser", "validpassword1234")
        result = self.user.log_in("loginuser", "validpassword1234")
        self.assertEqual(result, "Login successful")

    def test_log_in_failure(self):
        with self.assertRaises(ValueError):
            self.user.log_in("nonexistent", "wrongpassword")

    def test_delete_account_success(self):
        self.user.sign_up("deluser", "deletepassword1234", "del@example.com")
        result = self.user.delete_account("deluser", "deletepassword1234", "del@example.com")
        self.assertEqual(result, "Account deleted successfully")
        self.assertNotIn("deluser", self.user.users)

if __name__ == "__main__":
    unittest.main()
