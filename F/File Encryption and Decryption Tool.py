from cryptography.fernet import Fernet
import os

# Function to generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Function to write the key to a file
def write_key_to_file(key, filename='key.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

# Function to load the key from a file
def load_key(filename='key.key'):
    return open(filename, 'rb').read()

# Function to encrypt a file
def encrypt_file(file_path, key):
    cipher_suite = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Function to decrypt a file
def decrypt_file(file_path, key):
    cipher_suite = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    decrypted_data = cipher_suite.decrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

# Main function
def main():
    print("File Encryption and Decryption Tool")
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
    
    if choice == 'E':
        key = generate_key()
        write_key_to_file(key)
        file_path = input("Enter the path of the file to encrypt: ")
        encrypt_file(file_path, key)
        print(f'File "{file_path}" encrypted successfully.')
    
    elif choice == 'D':
        try:
            key_path = input("Enter the path of the key file: ")
            key = load_key(key_path)
            file_path = input("Enter the path of the file to decrypt: ")
            decrypt_file(file_path, key)
            print(f'File "{file_path}" decrypted successfully.')
        except Exception as e:
            print(f'Error: {e}')
    
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
