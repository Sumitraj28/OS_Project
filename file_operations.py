import os

# Dummy database for storing files
files = {}

def upload_file(username, filename, content):
    """Upload a file."""
    if filename in files:
        return False
    files[filename] = {'content': content, 'owner': username}
    return True

def download_file(username, filename):
    """Download a file."""
    if filename not in files or files[filename]['owner'] != username:
        return None
    return files[filename]['content']

def share_file(username, filename, recipient):
    """Share a file with another user."""
    if filename not in files or files[filename]['owner'] != username:
        return False
    # Placeholder for sharing logic
    return True