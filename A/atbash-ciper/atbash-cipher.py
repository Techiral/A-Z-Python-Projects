# The TABLE is a string containing uppercase letters from A to Z.
TABLE = ''.join(chr(x) for x in range(65, 91))

# Function to convert a given text using the Atbash cipher
def convert(text: str):
    # Convert the input text to uppercase for consistency
    text = text.upper()
    
    # Variable to store the ciphered text
    cipheredText = ""

    # Iterate through each character in the text
    for i in text:
        # Check if the character is in the Atbash cipher table
        if i in TABLE:
            # Find the index of the character in the table
            idx = TABLE.find(i)
            
            # Append the corresponding character from the reverse side of the table
            cipheredText += TABLE[25 - idx]
        else:
            # If the character is not in the table, leave it unchanged
            cipheredText += i
    
    # Return the final ciphered text
    return cipheredText

# Main function to take user input, convert, and print the result
def main():
    # Prompt the user for input
    text = input("Input Text: ")
    
    # Call the convert function and print the result
    print("Output Text: {}".format(convert(text)))

# Entry point of the program
if __name__ == '__main__':    
    # Call the main function when the script is executed
    main()
