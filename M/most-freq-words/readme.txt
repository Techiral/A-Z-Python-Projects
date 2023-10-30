# PDF Text Analysis using PyPDF2 and NLTK

This Python script is designed to analyze the text content of a PDF file, extract and tokenize the text, remove common stop words, and count the frequency of each word. It then prints the most common words in the PDF.

## Prerequisites

- Python 3.x
- PyPDF2 library (You can install it using `pip install PyPDF2`)
- NLTK library (You can install it using `pip install nltk`)
- NLTK data (You need to download the NLTK data using `nltk.download('punkt')`)

## Usage

1. Save your PDF file that you want to analyze as 'doc.pdf' in the same directory as this script.

2. Make sure the PyPDF2 and NLTK libraries are installed along with the NLTK data.

3. Run the script by executing it in your Python environment.

4. The script will open and read 'doc.pdf', tokenize the text, remove common English stop words, and display the 10 most frequent words in the PDF.

## Customization

- You can change the PDF file's name by modifying the `pdf_file` variable. Replace 'doc.pdf' with the filename of your choice.

- To change the number of most common words to display, modify the `most_common(10)` part in the `print` statement at the end of the script.

- You can further customize the script to suit your specific needs, such as saving the results to a file, performing more advanced text analysis, or incorporating natural language processing techniques.

Remember to acknowledge the usage of NLTK and PyPDF2 libraries in your project, and consult their respective documentation for more advanced functionality and options.

## Author

Atharva Kulkarni

