import hashlib

# Define the string to be hashed
string_to_hash = "Hello, world!"

# Create an instance of the MD5 hashing algorithm
hash_object = hashlib.md5()

# Update the hash object with the string to be hashed
hash_object.update(string_to_hash.encode())

# Get the hexadecimal representation of the hash
hex_dig = hash_object.hexdigest()

# Print the hash
print(hex_dig)
