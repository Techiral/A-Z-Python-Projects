def count_word_occurrences(file_path):
    # Initialize an empty dictionary to store word counts
    word_count = {}

    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            # Read each line from the file
            for line in file:
                # Split the line into words using whitespace as a delimiter
                words = line.split()
                for word in words:
                    # Remove punctuation and convert to lowercase for uniformity
                    word = word.strip('.,!?()-"\'').lower()
                    
                    # Check if the word is already in the dictionary
                    if word in word_count:
                        # If yes, increment the count
                        word_count[word] += 1
                    else:
                        # If no, add it to the dictionary with a count of 1
                        word_count[word] = 1

        # Close the fileP
        file.close()

        # Print unique words and their occurrences
        for word, count in word_count.items():
            print(f'{word}: {count}')

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Input file path (update this with the correct file path)
file_path = 'sample.txt'

# Call the function to count word occurrences
count_word_occurrences(file_path)
