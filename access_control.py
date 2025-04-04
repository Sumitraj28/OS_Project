def check_permission(username, filename):
    """Check if a user has permission to access a file."""
    from file_operations import files
    if filename not in files:
        return False
    return files[filename]['owner'] == username