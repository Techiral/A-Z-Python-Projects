import os
import sys
import argparse
import getpass
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding as sym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def derive_key(password, salt, key_size):
    # Derive a cryptographic key from the password
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=key_size // 8,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

def encrypt_file(input_file, output_file, password):
    # Generate salt and IV
    salt = os.urandom(16)
    iv = os.urandom(16)

    # Derive key
    key = derive_key(password, salt, 256)

    # Initialize cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Read input file and encrypt
    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        # Write salt and IV to the output file
        f_out.write(salt)
        f_out.write(iv)

        # Read the file in chunks
        while True:
            chunk = f_in.read(1024)
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                padder = sym_padding.PKCS7(128).padder()
                chunk = padder.update(chunk) + padder.finalize()
            encrypted_chunk = encryptor.update(chunk)
            f_out.write(encrypted_chunk)
        # Finalize encryption
        f_out.write(encryptor.finalize())

    print(f"File encrypted successfully: {output_file}")

def decrypt_file(input_file, output_file, password):
    with open(input_file, 'rb') as f_in:
        # Read salt and IV from the input file
        salt = f_in.read(16)
        iv = f_in.read(16)

        # Derive key
        key = derive_key(password, salt, 256)

        # Initialize cipher
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        # Prepare to write decrypted data
        try:
            with open(output_file, 'w+b') as f_out:
                # Read the encrypted file in chunks
                while True:
                    chunk = f_in.read(1024)
                    if len(chunk) == 0:
                        break
                    decrypted_chunk = decryptor.update(chunk)
                    f_out.write(decrypted_chunk)
                # Finalize decryption
                decrypted_chunk = decryptor.finalize()
                f_out.write(decrypted_chunk)
                # Remove padding
                f_out.seek(0)
                data = f_out.read()
                unpadder = sym_padding.PKCS7(128).unpadder()
                data = unpadder.update(data) + unpadder.finalize()
                f_out.seek(0)
                f_out.write(data)
                f_out.truncate()
            print(f"File decrypted successfully: {output_file}")
        except Exception as e:
            print("Decryption failed. Incorrect password or corrupted file.")
            # Ensure the file is closed before deletion
            if not f_out.closed:
                f_out.close()
            if os.path.exists(output_file):
                os.remove(output_file)


def main():
    parser = argparse.ArgumentParser(description='AES File Encryption Tool')
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Mode of operation')
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', nargs='?', help='Output file path')
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print("Input file does not exist.")
        sys.exit(1)

    if not args.output_file:
        # Generate default output file name
        if args.mode == 'encrypt':
            args.output_file = args.input_file + '.enc'
        else:
            if args.input_file.endswith('.enc'):
                args.output_file = args.input_file[:-4]
            else:
                args.output_file = args.input_file + '.dec'

    password = getpass.getpass(prompt='Enter password: ')

    if args.mode == 'encrypt':
        encrypt_file(args.input_file, args.output_file, password)
    else:
        decrypt_file(args.input_file, args.output_file, password)

if __name__ == '__main__':
    main()
