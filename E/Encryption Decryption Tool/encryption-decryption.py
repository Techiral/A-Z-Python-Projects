from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def encrypt_file(input_file_path, output_file_path, password):
    # Generate a key and IV from the password using SHA-256
    key = hashlib.sha256(password.encode()).digest()
    iv = b'\x00' * 16

    # Create an AES cipher object with the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Read the input file and encrypt the contents
    with open(input_file_path, 'rb') as input_file:
        input_data = input_file.read()
        padded_data = pad(input_data, AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)

    # Write the encrypted data to the output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(encrypted_data)

def decrypt_file(input_file_path, output_file_path, password):
    # Generate a key and IV from the password using SHA-256
    key = hashlib.sha256(password.encode()).digest()
    iv = b'\x00' * 16

    # Create an AES cipher object with the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Read the input file and decrypt the contents
    with open(input_file_path, 'rb') as input_file:
        input_data = input_file.read()
        decrypted_data = cipher.decrypt(input_data)
        unpadded_data = unpad(decrypted_data, AES.block_size)

    # Write the decrypted data to the output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(unpadded_data)

# Example usage: encrypt a file
encrypt_file('input.txt', 'encrypted.bin', 'password123')

# Example usage: decrypt a file
decrypt_file('encrypted.bin', 'decrypted.txt', 'password123')
