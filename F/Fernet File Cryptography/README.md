# File Encryption and Decryption Tool

This Python-based tool provides an easy way to secure your files through encryption and decryption processes. It uses the Fernet symmetric encryption scheme from the `cryptography` library to ensure data privacy and protection. Whether you need to safeguard sensitive documents or decrypt encrypted files, this tool offers a simple and effective solution.

## Getting Started

Before using the tool, make sure you have Python installed on your system. You can install the required library using the following command:

```bash
pip install cryptography


## Usage
# Encryption
. Run the script: python encryption_tool.py
. Choose 'E' to encrypt a file.
. Enter the file path you want to encrypt.
.The tool will generate a unique encryption key and save it to key.key. Your file will be encrypted securely.
# Decryption
. Run the script: python encryption_tool.py
. Choose 'D' to decrypt a file.
. Provide the path to the key file (usually key.key) used for encryption.
. Enter the file path you want to decrypt.
. The tool will decrypt the file, restoring the original data.