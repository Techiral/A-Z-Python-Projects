# Import Libraries
from PyPDF4 import PdfFileReader, PdfFileWriter, utils
import os
import argparse
import getpass
from io import BytesIO
import pyAesCrypt

# Size of chunk for encryption/decryption
BUFFER_SIZE = 64 * 1024


def is_encrypted(input_file: str) -> bool:
    """Check if the input file is encrypted using PyPDF4 library."""
    with open(input_file, 'rb') as pdf_file:
        pdf_reader = PdfFileReader(pdf_file, strict=False)
        return pdf_reader.isEncrypted


def encrypt_pdf(input_file: str, password: str):
    """
    Encrypts a PDF file using PyPDF4 library.
    Precondition: File is not encrypted.
    """
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(open(input_file, 'rb'), strict=False)
    if pdf_reader.isEncrypted:
        print(f"PDF File {input_file} is already encrypted")
        return False, None, None
    try:
        # Copy all pages to the writer object for encryption
        for page_number in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_number))
    except utils.PdfReadError as e:
        print(f"Error reading PDF File {input_file}: {e}")
        return False, None, None

    # Encrypt the PDF with the provided password
    pdf_writer.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)
    return True, pdf_reader, pdf_writer


def decrypt_pdf(input_file: str, password: str):
    """
    Decrypts an encrypted PDF file using PyPDF4 library.
    Precondition: File is already encrypted.
    """
    pdf_reader = PdfFileReader(open(input_file, 'rb'), strict=False)
    if not pdf_reader.isEncrypted:
        print(f"PDF File {input_file} is not encrypted")
        return False, None, None

    # Decrypt the PDF with the provided password
    pdf_reader.decrypt(password=password)
    pdf_writer = PdfFileWriter()
    try:
        # Copy all pages to the writer object for decryption
        for page_number in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_number))
    except utils.PdfReadError as e:
        print(f"Error reading PDF File {input_file}: {e}")
        return False, None, None

    return True, pdf_reader, pdf_writer


def cipher_stream(input_buffer: BytesIO, password: str):
    """Encrypts an input memory buffer and returns an encrypted output memory buffer."""
    # Initialize the output encrypted binary stream
    output_buffer = BytesIO()
    input_buffer.seek(0)

    # Encrypt the stream
    pyAesCrypt.encryptStream(input_buffer, output_buffer, password, BUFFER_SIZE)
    output_buffer.seek(0)
    return output_buffer


def decipher_file(input_file: str, output_file: str, password: str):
    """
    Decrypts an encrypted input file and saves the decrypted content to an output file.
    """
    input_file_size = os.stat(input_file).st_size
    output_buffer = BytesIO()

    with open(input_file, mode='rb') as input_buffer:
        try:
            # Decrypt the stream
            pyAesCrypt.decryptStream(
                input_buffer, output_buffer, password, BUFFER_SIZE, input_file_size)
        except Exception as e:
            print("Exception", str(e))
            return False

    if output_buffer:
        with open(output_file, mode='wb') as f:
            f.write(output_buffer.getbuffer())

    return True


def encrypt_decrypt_file(**kwargs):
    """Encrypts or decrypts a file."""
    input_file = kwargs.get('input_file')
    password = kwargs.get('password')
    output_file = kwargs.get('output_file')
    action = kwargs.get('action')

    # Protection Level
    # Level 1 --> Encryption / Decryption using PyPDF4
    # Level 2 --> Encryption and Ciphering / Deciphering and Decryption
    level = kwargs.get('level')

    if not output_file:
        output_file = input_file

    if action == "encrypt":
        result, pdf_reader, pdf_writer = encrypt_pdf(
            input_file=input_file, password=password)

        # Encryption completed successfully
        if result:
            output_buffer = BytesIO()
            pdf_writer.write(output_buffer)
            pdf_reader.stream.close()

            if level == 2:
                output_buffer = cipher_stream(output_buffer, password=password)

            with open(output_file, mode='wb') as f:
                f.write(output_buffer.getbuffer())

    elif action == "decrypt":
        if level == 2:
            decipher_file(input_file=input_file,
                          output_file=output_file, password=password)

        result, pdf_reader, pdf_writer = decrypt_pdf(
            input_file=input_file, password=password)

        # Decryption completed successfully
        if result:
            output_buffer = BytesIO()
            pdf_writer.write(output_buffer)
            pdf_reader.stream.close()

            with open(output_file, mode='wb') as f:
                f.write(output_buffer.getbuffer())


class Password(argparse.Action):
    """Hides the password entry."""
    def __call__(self, parser, namespace, values, option_string):
        if values is None:
            values = getpass.getpass()
        setattr(namespace, self.dest, values)


def is_valid_path(path):
    """Validates the input path and checks whether it is a file path or a folder path."""
    if not path:
        raise ValueError("Invalid Path")
    if os.path.isfile(path) or os.path.isdir(path):
        return path
    else:
        raise ValueError(f"Invalid Path {path}")


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a PDF file.")
    parser.add_argument("file", help="Input PDF file you want to encrypt or decrypt", type=is_valid_path)
    parser.add_argument('-a', '--action', dest='action', choices=['encrypt', 'decrypt'],
                        type=str, default='encrypt', help="Choose whether to encrypt or to decrypt")
    parser.add_argument('-l', '--level', dest='level', choices=[1, 2], type=int,
                        default=1, help="Choose which protection level to apply")
    parser.add_argument('-p', '--password', dest='password', action=Password,
                        nargs='?', type=str, required=True, help="Enter a valid password")
    parser.add_argument('-o', '--output_file', dest='output_file',
                        type=str, help="Enter a valid output file")

    args = vars(parser.parse_args())

    # Display command arguments except for the password
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i, j)
                   for i, j in args.items() if i != 'password'))
    print("######################################################################")

    return args


if __name__ == '__main__':
    # Parse command-line arguments entered by the user
    args = parse_args()

    # Encrypting or Decrypting the file
    encrypt_decrypt_file(
        input_file=args['file'], password=args['password'],
        action=args['action'], level=args['level'], output_file=args['output_file']
    )
