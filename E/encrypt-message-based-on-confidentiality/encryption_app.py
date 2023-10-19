import hashlib

def get_confidentiality_level():
    while True:
        try:
            level = int(input("Enter the confidentiality level (1-10): "))
            if 1 <= level <= 10:
                return level
            else:
                print("Confidentiality level must be between 1 and 10.")
        except ValueError:
            print("Please enter a valid integer between 1 and 10.")

def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_message += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                encrypted_message += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_message += char
    return encrypted_message, "Caesar Cipher"

def encrypt_message(message, confidentiality_level):
    if 1 <= confidentiality_level <= 2:
        # Caesar cipher with a shift of 1 for low confidentiality
        shift = 1
        encrypted_message, method = caesar_cipher_encrypt(message, shift)
    else:
        # Choose a suitable hashing algorithm based on the level
        if 2 <= confidentiality_level <= 4:
            hash_algorithm = hashlib.sha256
        elif 4 < confidentiality_level <= 6:
            hash_algorithm = hashlib.sha384
        elif 6 < confidentiality_level <= 8:
            hash_algorithm = hashlib.sha3_256
        else:
            hash_algorithm = hashlib.sha512

        # Hashing the message
        hashed_message = hash_algorithm(message.encode()).hexdigest()
        encrypted_message, method = hashed_message, hash_algorithm.__name__

    return encrypted_message, method

def main():
    message = input("Enter the message to be encrypted: ")
    confidentiality_level = get_confidentiality_level()

    encrypted_message, method = encrypt_message(message, confidentiality_level)
    print(f"Encrypted message: {encrypted_message}")
    print(f"Encryption method used: {method}")

if __name__ == "__main__":
    main()
