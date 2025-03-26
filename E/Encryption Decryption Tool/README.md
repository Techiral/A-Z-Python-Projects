# Encryption-Decryption-Tool

Project: Simple File Encryption and Decryption Tool

Description: This project will allow the user to encrypt and decrypt a file using a password-based encryption scheme with the AES encryption algorithm. The user will provide a file to encrypt or decrypt, along with a password, and the program will use the PyCryptodome library to encrypt or decrypt the file using the AES algorithm with the provided password.

Explanation:

    The hashlib module is used to generate a key and IV from the user-provided password using the SHA-256 hashing algorithm. The key and IV are generated as bytes objects.
    The Crypto.Cipher.AES class is used to create an AES cipher object with the generated key and IV in CBC mode.
    The Crypto.Util.Padding module is used to pad the input data to a multiple of the AES block size (16 bytes), and unpad the decrypted data after decryption.
    The open() function is used to read and write data to files, with the rb and wb flags indicating binary mode.
    The pad() and unpad() functions are used to ensure that the data is padded to the correct block size for encryption and correctly unpadded after decryption.

Note that this is just a simple example of a file encryption and decryption tool. In a real-world scenario, there are many additional considerations for building a secure file encryption tool, such as securely generating and storing the key and IV, using authenticated encryption modes, protecting against side-channel attacks, and more. It's important to carefully consider these factors and follow best practices for secure coding and encryption.
