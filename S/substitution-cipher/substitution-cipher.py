import random

# Define the original mapping table as uppercase letters A-Z
TABLE = ''.join(chr(ch) for ch in range(65, 91))

# Generate a random permutation of the mapping table to create the substitution key
KEY = random.sample(TABLE, 26)

def encrypt(inputText: str):
    # Convert the input text to uppercase for consistency
    inputText = inputText.upper()
    
    # Initialize an empty string to store the encrypted output
    outputText = ''

    # Iterate through each character in the input text
    for i in inputText:
        # Check if the character is in the original mapping table
        if i in TABLE:
            # If yes, substitute the character with its corresponding character from the key
            outputText += KEY[ord(i) - 65]
        else:
            # If not in the mapping table, keep the character unchanged
            outputText += i

    # Print the original mapping table
    print('MAP_KEYS:  {}'.format(TABLE))

    # Print the substitution key
    print('MAP_ITEMS: {}'.format(''.join(c for c in KEY)))

    # Print the encrypted output text
    print('Output Text: {}'.format(outputText))

def main():
    # Get input text from the user
    inputText = input('Input Text: ')

    # Encrypt the input text and display the result
    encrypt(inputText)

if __name__ == '__main__':
    # Execute the main function when the script is run
    main()
