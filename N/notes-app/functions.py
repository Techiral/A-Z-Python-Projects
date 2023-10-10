import os

def create_file(title,content):
    """
    This function creates a text file in the 'created-notes' directory with the given title and content.
    If the directory doesn't exist, it will be created.
    After creating the file, it prompts the user to print the content in the terminal.
    """
    directory = 'N/notes-app/created-notes/'
    filename = title.lower() + ".txt"
    final_content = title.upper() + "\n\n" + content

    # Ensuring that the directory exists and if it doesn't, creating it
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Combining the directory and filename to get the full file path
    file_path = os.path.join(directory, filename)

    with open(file_path, 'w') as file:
        file.write(final_content)
    print("\nContent written successfully!! in " + filename+"\n")

    to_print = input("SHOULD I PRINT IT IN THE TERMINAL?(Y for yes) ")
    if to_print=='Y' or to_print=='y':
        with open(file_path, 'r') as file:
            printing_content = file.read()
            print('\n'+'-'*50+'\n'+' '*20+'YOUR NOTE\n'+'-'*50)
            print(printing_content)


def view_note(title):
    """
    This function prints the contents of the text file with given title if the file exists.
    If file doesn't exists, it prints error message.
    """
    filename = title.lower() + '.txt'
    directory = 'N/notes-app/created-notes/'
    try:
        with open(directory+filename, 'r') as file:
            print_contents = file.read()
            print('\n'+'-'*50+'\n'+' '*20+'YOUR NOTE\n'+'-'*50)
            print(print_contents)
    except FileNotFoundError:
        print('\n'+'-'*50+'\n'+' '*20+'ERROR\n'+'-'*50)
        print("No such text file available !!!")


def delete_note(title):
    """
    This function deletes                                                         the text file with given title if the file exists.
    If file doesn't exists, it prints error message.
    """
    filename = title.lower() + '.txt'
    directory = 'N/notes-app/created-notes/'
    file_path = directory + filename
    if os.path.exists(file_path):
        os.remove(file_path) # Deleting the file
        print('\n'+'-'*50+'\n'+' '*20+'DELETED\n'+'-'*50)
        print(filename+ "successfully deleted !!!")

    else:
        print('\n'+'-'*50+'\n'+' '*20+'ERROR\n'+'-'*50)
        print("No such text file available !!!")

    
