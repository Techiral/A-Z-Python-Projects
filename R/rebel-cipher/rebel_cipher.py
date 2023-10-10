
def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            is_uppercase = char.isupper()
            char = char.upper()
            encrypted_char = chr((ord(char) - 65 + key) % 26 + 65)
            if not is_uppercase:
                encrypted_char = encrypted_char.lower()
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(encrypted_message, key):
    return encrypt(encrypted_message, -key)


def save_to_file(data, filename):
    with open(filename, "w") as file:
        file.write(data)


def read_from_file(filename):
    with open(filename, "r") as file:
        return file.read()


# Main program
valid_message = False
while not valid_message:
    message = input("Enter a message: ")
    if any(char.isdigit() for char in message):
        print("Invalid message! Please enter a message without numbers.")
    else:
        valid_message = True

key = int(input("Enter the encryption key: "))

encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)

save_to_file(encrypted_message, "encrypted_message.txt")

encrypted_message_from_file = read_from_file("encrypted_message.txt")
print("Read from file:", encrypted_message_from_file)
