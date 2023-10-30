Add Full Stops to Sentences in Text Files
This Python script is designed to process text files within a specified input folder and add full stops to the end of sentences where needed. It is particularly useful for text in languages that do not consistently use full stops to denote the end of sentences.

How to Use
Input Folder: Before running the script, replace "input folder" with the path to the directory containing your input text files. These text files should be in the UTF-8 encoding.

Output Folder: Replace "output folder" with the path to the directory where you want the modified text files to be saved.

Run the Script: Execute the script, and it will process each text file in the input folder. For each file, it will:

Split the content into sentences using common punctuation marks and newline characters as delimiters (e.g., '.', '!', '?', and '\n').

Remove leading and trailing whitespace from each sentence.

Add a full stop to the end of a sentence if it doesn't already end with one.

Save the modified content to a new file in the output folder.

Result: After the script completes, you will find modified text files in the output folder with full stops added to sentences as needed.

Example
Suppose you have a text file in the input folder with the following content:

This is a sample sentence without a full stop
This is another sentence with a full stop.
After running the script, the content of the output file in the output folder will be:


This is a sample sentence without a full stop.
This is another sentence with a full stop.

Dependencies
The script uses the following Python libraries:
os: For interacting with the file system.
re: For regular expression-based text splitting.
Note
This script uses a simple approach to identify sentence boundaries based on common punctuation marks. It may not handle all sentence structures perfectly, especially for languages with complex grammar rules. You may need to adapt the script according to the specific requirements of your text data.

Ensure you have Python installed on your system to run this script.

Caution: Always back up your original data before running this script, as it modifies the text files in the input folder.
