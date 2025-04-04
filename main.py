from user_auth import register_user, login
from file_operations import upload_file, download_file, share_file
from access_control import check_permission

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Upload File\n4. Download File\n5. Share File\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if register_user(username, password):
                print("User registered successfully.")
            else:
                print("Registration failed.")

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login(username, password):
                print("Login successful.")
            else:
                print("Login failed.")

        elif choice == '3':
            username = input("Enter username: ")
            filename = input("Enter filename: ")
            content = input("Enter file content: ")
            if upload_file(username, filename, content):
                print("File uploaded successfully.")
            else:
                print("Failed to upload file.")

        elif choice == '4':
            username = input("Enter username: ")
            filename = input("Enter filename: ")
            content = download_file(username, filename)
            if content:
                print(f"File content: {content}")
            else:
                print("Failed to download file.")

        elif choice == '5':
            username = input("Enter username: ")
            filename = input("Enter filename: ")
            recipient = input("Enter recipient username: ")
            if share_file(username, filename, recipient):
                print("File shared successfully.")
            else:
                print("Failed to share file.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()