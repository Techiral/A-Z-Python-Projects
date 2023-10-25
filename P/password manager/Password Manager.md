# Password Manager

This is a simple command-line password manager in Python.

## Features

- Secure storage and retrieval of passwords.
- Easy-to-use command-line interface.
- Strong encryption using the Fernet library.

## Installation

1. Ensure you have Python installed on your system.
2. Clone this repository or download the source code.
3. Install the required libraries using pip:

   ```bash
   pip install cryptography
   ```

## Usage

1. You will be prompted to enter a master password. This password will be used to encrypt and decrypt your stored passwords.

2. Use the following options:
   - **Add Password**: Add a new password entry.
   - **View Password**: View a previously added password.
   - **List Passwords**: List all stored passwords.
   - **Delete Password**: Delete a stored password.
   - **Quit**: Exit the password manager.

## Security

- Ensure that your master password is strong and unique. This password is used to protect your stored passwords.
- Be cautious with the master password. If you forget it, there is no way to recover your stored passwords.
