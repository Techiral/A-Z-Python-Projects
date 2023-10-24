from cryptography.fernet import Fernet
import json
import os

class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password.encode()
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.passwords = {}

    def save_password(self, website, username, password):
        encrypted_password = self.fernet.encrypt(password.encode())
        self.passwords[website] = {
            "username": username,
            "password": encrypted_password.decode()
        }
        self._save_data()

    def get_password(self, website):
        if website in self.passwords:
            encrypted_password = self.passwords[website]["password"]
            password = self.fernet.decrypt(encrypted_password.encode()).decode()
            return password
        else:
            return None

    def _save_data(self):
        data = {
            "master_password": self.master_password.decode(),
            "key": self.key.decode(),
            "passwords": self.passwords
        }
        with open("passwords.json", "w") as file:
            json.dump(data, file)

    def load_data(self):
        if os.path.exists("passwords.json"):
            with open("passwords.json", "r") as file:
                data = json.load(file)
                self.master_password = data["master_password"].encode()
                self.key = data["key"].encode()
                self.fernet = Fernet(self.key)
                self.passwords = data["passwords"]

# Example usage:
if __name__ == "__main__":
    master_password = input("Enter your master password: ")
    password_manager = PasswordManager(master_password)

    while True:
        print("1. Save Password")
        print("2. Get Password")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter the website: ")
            username = input("Enter your username: ")
            password = input("Enter the password: ")
            password_manager.save_password(website, username, password)
        elif choice == "2":
            website = input("Enter the website: ")
            password = password_manager.get_password(website)
            if password:
                print(f"Password for {website}: {password}")
            else:
                print(f"Password for {website} not found.")
        elif choice == "3":
            break
