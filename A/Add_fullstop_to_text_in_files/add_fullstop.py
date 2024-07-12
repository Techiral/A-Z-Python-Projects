import os
import re

def add_full_stops(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all text files in the input folder
    input_files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]

    for input_file in input_files:
        input_file_path = os.path.join(input_folder, input_file)
        output_file_path = os.path.join(output_folder, input_file)

        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Split the content into sentences using common punctuation marks as delimiters
        sentences = re.split(r'[।!?\n]', content)

        # Initialize the output content
        output_content = ''

        # Iterate through each sentence
        for sentence in sentences:
            # Remove leading and trailing whitespace
            sentence = sentence.strip()

            # Skip empty sentences
            if not sentence:
                continue

            # Add a full stop if the sentence doesn't already end with one
            if not sentence.endswith('.') and not sentence.endswith('!') and not sentence.endswith('?'):
                sentence += '.'

            # Add the sentence to the output content
            output_content += sentence + '\n'

        # Write the modified content to the output file
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(output_content)

if __name__ == "__main__":
    input_folder = "input folder"  # Replace with the path to your input folder
    output_folder = "output folder"  # Replace with the path to your output folder

    add_full_stops(input_folder, output_folder)
    print("Full stops added to sentences in the input files. Output saved in the output folder.")
