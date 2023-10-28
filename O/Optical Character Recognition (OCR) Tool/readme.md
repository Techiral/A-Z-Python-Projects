# OCR Tool using Tesseract

## Overview

This Python application is a simple Optical Character Recognition (OCR) tool that uses the Tesseract OCR engine to extract text from images. It takes an image file as input, processes it, and prints the extracted text to the console.

## Prerequisites

Before using this tool, ensure you have the following software and libraries installed:

- Tesseract OCR: Install Tesseract OCR from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract) or using package managers like [apt](https://github.com/tesseract-ocr/tesseract) or [Homebrew](https://formulae.brew.sh/formula/tesseract).

- Python 3: This application is written in Python. You can download it from [Python's official website](https://www.python.org/downloads/).

- Python Libraries: Make sure you have the following Python libraries installed using `pip`:
  - `pytesseract`: Run `pip install pytesseract` to install it.
  - `Pillow` (PIL): Run `pip install Pillow` to install it.

## Usage

1. Clone this repository or download the `ocr_tool.py` file to your local machine.

2. Open a terminal or command prompt.

3. Run the OCR tool by executing the following command, replacing `'your_image.png'` with the path to your image file:

   ```shell
   python ocr_tool.py your_image.png
