# Password Generator

A Python script for generating random passwords with various configurations. You can specify the number of digits, lowercase characters, uppercase characters, and special characters in the generated passwords. Additionally, you can generate completely random passwords with a specific total length.

## Usage

### Requirements

- Python 3

### Running the Script

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script with the desired options.

#### Command Line Options

- `-n` or `--numbers`: Number of digits in the password.
- `-l` or `--lowercase`: Number of lowercase characters in the password.
- `-u` or `--uppercase`: Number of uppercase characters in the password.
- `-s` or `--special-chars`: Number of special characters in the password.
- `-t` or `--total-length`: The total password length. If provided, it overrides other character count options.
- `-a` or `--amount`: Number of passwords to generate (default is 1).
- `-o` or `--output-file`: Name of the output file to store generated passwords (optional).

#### Examples

Generate a single password with 8 digits, 4 lowercase letters, 2 uppercase letters, and 2 special characters:

```bash
python password_generator.py -n 8 -l 4 -u 2 -s 2
```
Generate 5 passwords with a total length of 16 characters each:
```bash
python password_generator.py -t 16 -a 5
```
Generate a single completely random password with a total length of 20 characters:
```bash
python password_generator.py -t 20
```
Save the generated passwords to an output file:
```bash
python password_generator.py -n 8 -l 4 -u 2 -s 2 -o passwords.txt
```

#### License
There's no information about the license. If you are original author of this code, please raise an issue.

---

Feel free to use this password generator to create strong and secure passwords for your needs. If you have any suggestions or encounter issues, please open an issue in this repository.

