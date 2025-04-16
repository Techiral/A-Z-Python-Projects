# Word Occurrence Counter

This is a Python program that reads a text file, identifies unique words, and counts how many times each word appears in the file.

## How to Use

1. **Prerequisites:**
   - Ensure you have Python installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download:**
   - Clone this repository or download the code as a ZIP file and extract it to your desired location.

3. **Prepare Your Text File:**
   - Create a text file or use an existing one that you want to analyze. Make sure the file is in plain text format with words separated by spaces or other whitespace characters.

4. **Edit the Code (Optional):**
   - If you want to customize the code or use a different text file, open the `word_occurrence_counter.py` file and update the `file_path` variable with the path to your text file.


### **Important Note**
   ### How to find the path to your text file?

   - Check the File Path: Ensure that the file path you provided in your Python script is correct. You should specify the correct path to the 'sample.txt' file on your system.
   - Or you can simply just add the 'sample.txt' file to the directory in which your python code is saved.
   And, let the 'sample.txt' file be as it is in the code.

   - Or if you want to just simple add the path in 'file_path' variable Just simply go the sample.txt file where you have saved it. And, right click on it and select properties and there you go the location is visible.

   Also, while mentioning the file_path few points to learn:

   - In Windows file paths, you often see double backslashes (\\) when specifying directory paths in Python code. This is because the backslash is an escape character in Python strings. An escape character is used to represent characters that are difficult or impossible to type directly, such as a newline or a tab. For example, you use "\n" to represent a newline character.
   When specifying file paths in Windows, you use backslashes to separate directories in the path, like this:
   ```
   file_path = 'D:\Open source\A-Z-Python-Projects\W\Word Occurrence Counter\sample.txt'
   ```
   - However, a single backslash is also used as an escape character in Python strings. So, if you write the path like this:
   ```
   file_path = 'D:\Open source\A-Z-Python-Projects\W\Word Occurrence Counter\sample.txt'
   ```
   - Python interprets the backslashes as escape characters, and this could lead to unintended consequences. For example, '\W' would be interpreted as an escape sequence representing a non-printable character.

   - The double backslashes indicate to Python that you want to treat each backslash as a literal character, not as an escape sequence. It ensures that the path is interpreted correctly and that the backslashes in the file path are not misinterpreted.




5. **Run the Program:**
   - Open a terminal or command prompt.
   - Navigate to the directory where you saved the code and text file.
   - Run the program by entering the following command:

     ```
     python word_occurrence_counter.py
     ```

   - The program will read the text file and display the unique words along with their occurrences.

6. **Review the Results:**
   - The program will print the unique words and their counts in the terminal.

## Example

Suppose you have a text file named `sample.txt` with the following content:

This is a sample text file. It contains some words that will be used for testing.
You can modify this file or create your own text file for testing the program.

```
Running the program with this file will produce the following output:
```

```
Output:
this: 1
is: 1
a: 1
sample: 1
text: 1
file: 1
it: 1
contains: 1
some: 1
words: 1
that: 1
will: 1
be: 1
used: 1
for: 1
testing: 2
you: 1
can: 1
modify: 1
your: 1
own: 1
the: 1
program: 1
```








## License

#### This code is provided under the [MIT License](LICENSE).



### Feel free to adjust the README file as needed, add more details, or include any specific instructions for your users. This README provides a basic explanation of how to use the code and what to expect when running it.