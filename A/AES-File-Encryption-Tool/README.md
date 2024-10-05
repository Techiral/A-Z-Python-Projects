# AES Encryption Tool

This tool provides a simple interface to encrypt and decrypt files using the AES (Advanced Encryption Standard) encryption algorithm. It uses the AES-CBC mode for encryption, ensuring that your data remains secure and private. A password-based key derivation function (PBKDF2 with HMAC-SHA256) is used to derive the encryption key from the provided password, adding another layer of security.

## Features

- **Encrypt Files**: Securely encrypt any file with a password.
- **Decrypt Files**: Decrypt previously encrypted files using the same password.
- **Automatic Padding**: Automatically handles file padding to ensure proper encryption even for files that are not a multiple of the AES block size.
- **Salt and IV Generation**: Generates a random salt and initialization vector (IV) for each encryption to enhance security.

## Installation

### Prerequisites:

1. Python 3.x
2. `cryptography` package

### To install the required package:

```bash
pip install cryptography
```

## Usage

### Command-line Arguments

- `mode`: Choose between `encrypt` or `decrypt` mode.
- `input_file`: The path to the file you want to encrypt or decrypt.
- `output_file` (optional): The desired path for the encrypted or decrypted output file. If not provided, the tool will generate a default name:
  - For encryption: `input_file.enc`
  - For decryption: If the input file ends with `.enc`, it will remove this extension, otherwise it appends `.dec`.

### Encrypting a File

```bash
python aes_tool.py encrypt <input_file> <output_file>
```

**Example:**

```bash
python aes_tool.py encrypt example.txt
```

This will prompt you for a password and create an encrypted file called `example.txt.enc`.

### Decrypting a File

```bash
python aes_tool.py decrypt <input_file> <output_file>
```

**Example:**

```bash
python aes_tool.py decrypt example.txt.enc
```

This will prompt you for the password and decrypt the file to `example.txt`.

### Important Notes:

- You must remember the password used for encryption. The same password is required for decryption.
- If you provide an incorrect password during decryption, the tool will notify you of the failure and delete any incomplete output files to prevent corruption.

## How It Works

1. **Encryption:**

   - The tool generates a random 16-byte salt and initialization vector (IV).
   - The salt is used with PBKDF2HMAC (HMAC-SHA256) to derive a cryptographic key from the password.
   - AES encryption (in CBC mode) is applied to the input file data.
   - The encrypted file contains the salt, IV, and the encrypted data.

2. **Decryption:**
   - The tool reads the salt and IV from the encrypted file.
   - It derives the cryptographic key using the same password-based key derivation function (PBKDF2HMAC).
   - AES decryption is applied, and the original file content is recovered.

## Author

- **Name**: Aswin P Kumar
- **GitHub**: [AswinPKumar01](https://github.com/AswinPKumar01)

---
