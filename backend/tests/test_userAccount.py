"""
Unit tests for app.userAccount.User.

These tests use a temporary SQLite file for isolation. They set the module's
DB path to the temporary file, create a minimal `accounts` table required by
the implementation, then exercise sign_up, log_in, update_profile and
delete_account.

Run from the repository root:

  cd backend
  python3 -m unittest tests/test_userAccount.py

  
Noted: Generated useing GitHub Copilot
Prompt: Update the unit tests for userAccount.py to reflect the changes made in the methods.
"""

import os
import sqlite3
import tempfile
import unittest

from app import userAccount
from app.userAccount import User


class TestUserAccount(unittest.TestCase):
    def setUp(self):
        # Create a temporary database file and point the module to it
        fd, self.db_path = tempfile.mkstemp(prefix="test_eventplanner_", suffix=".db")
        os.close(fd)
        userAccount.DB_NAME = self.db_path

        # Create a minimal accounts table used by the implementation
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE accounts (
                BearID INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                recoveryEmail TEXT
            )
            """
        )
        conn.commit()
        conn.close()

    def tearDown(self):
        try:
            os.remove(self.db_path)
        except OSError:
            pass

    def _get_user_row(self, username):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT username, password, recoveryEmail FROM accounts WHERE username = ?", (username,))
        row = cur.fetchone()
        conn.close()
        return row

    def test_sign_up_success_and_db_entry(self):
        User.sign_up("alice", "verylongpassword12345", "alice@example.com")
        row = self._get_user_row("alice")
        self.assertIsNotNone(row)
        self.assertEqual(row[0], "alice")
        self.assertEqual(row[2], "alice@example.com")

    def test_sign_up_existing_username_raises(self):
        # Insert a user directly then try signing up with same username
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("INSERT INTO accounts (username, password, recoveryEmail) VALUES (?, ?, ?)",
                    ("bob", "passwordforbob12345", "bob@example.com"))
        conn.commit()
        conn.close()

        with self.assertRaises(ValueError):
            User.sign_up("bob", "anotherlongpassword123", "bob2@example.com")

    def test_sign_up_short_password_raises(self):
        with self.assertRaises(ValueError):
            User.sign_up("shorty", "shortpwd", "short@example.com")

    def test_sign_up_invalid_email_raises(self):
        with self.assertRaises(ValueError):
            User.sign_up("charlie", "sufficientlengthpwd123", "not-an-email")

    def test_log_in_success_and_failure(self):
        User.sign_up("dave", "davesuperlongpass123", "dave@example.com")
        result = User.log_in("dave", "davesuperlongpass123")
        self.assertEqual(result, "Login successful")

        with self.assertRaises(ValueError):
            User.log_in("dave", "wrongpassword")

    def test_update_profile_updates_db_and_instance(self):
        username = "eve"
        password = "evestrongpassword123"
        email = "eve@example.com"
        User.sign_up(username, password, email)

        # Create an instance for the same username and update
        u = User(username=username, password=password, email=email)
        u.update_profile(new_email="eve2@example.com", new_password="newstrongpassword456")

        # Verify instance fields updated
        self.assertEqual(u.email, "eve2@example.com")
        self.assertEqual(u.password, "newstrongpassword456")

        # Verify DB updated
        row = self._get_user_row(username)
        self.assertEqual(row[1], "newstrongpassword456")
        self.assertEqual(row[2], "eve2@example.com")

    def test_delete_account_success_and_not_found(self):
        User.sign_up("frank", "frankspassword12345", "frank@example.com")
        result = User.delete_account("frank", "frankspassword12345", "frank@example.com")
        self.assertEqual(result, "Account deleted successfully")

        # Deleting again should raise
        with self.assertRaises(ValueError):
            User.delete_account("frank", "frankspassword12345", "frank@example.com")


if __name__ == "__main__":
    unittest.main()
