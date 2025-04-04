import hashlib
import os

# Dummy database for storing user credentials
users = {}

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    """Register a new user."""
    if username in users:
        return False
    users[username] = hash_password(password)
    return True

def login(username, password):
    """Authenticate a user."""
    if username not in users:
        return False
    return users[username] == hash_password(password)