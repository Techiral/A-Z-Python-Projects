# Plagiarism-checker-Python

This repo consists of a source code of a Python script which detects plagiarism in a textual document using **cosine similarity**.

## How is it Done?

You might be wondering how plagiarism detection on textual data is done, well it ain't as complicated as you may think.

We all know that computers are good with numbers; so in order to compute the similarity between two text documents, the textual raw data is transformed into vectors => arrays of numbers and from that, we make use of basic knowledge of vectors to compute the similarity between them.

This repo contains a basic example on how to do that.

## Dependencies

Before you begin playing with the source code, you might need to install dependencies just as shown below;

```bash
pip3 install -r requirements.txt
```

## Running the App

To run this code you need to have your textual documents in your project directory with the **.txt** extension. When you run the script, it will automatically load all the documents with that extension and then compute the similarities between them as shown below;

## Credits

All the credit goes to [kalebu](https://github.com/kalebu).
