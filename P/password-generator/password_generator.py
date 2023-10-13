import random
import string

def generate_password(length=12):
    # Define character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure a minimum length of 8 characters
    if length < 8:
        length = 8

    # Generate a random password using random.sample to ensure uniqueness
    password = random.sample(all_characters, length)

    # Convert the password list to a string
    password = ''.join(password)

    return password

# Example usage:
password = generate_password()
print("Generated Password:", password)
