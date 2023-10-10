import sys
from functions import *

# Initializing a flag variable for running of the application
is_running = True

while is_running:
    # Displaying information on the screen
    print('\n')
    print(" "*20+"WELCOME TO NOTES APP")
    print('-'*50)
    print('Your options are:')
    print('1. Create a note')
    print('2. View a note')
    print('3. Delete a note')
    print('4. Exit \n')
    try:
        option = int(input("Select one option(1/2/3/4): "))
        if option == 1:
            title = input("Enter the tile for your note: ")
            content = input("Enter the content: \n")
            create_file(title,content) 
        elif option == 2:
            title = input("Enter the tile of the note that you want to view: ")
            view_note(title)
        elif option == 3:
            title = input("Enter the tile of the note that you want to delete: ")
            delete_note(title)
        elif option == 4:
            sys.exit()
    except ValueError:
        print('\n'+'-'*50+'\n'+' '*20+'ERROR\n'+'-'*50)
        print("Enter 1/2/3/4 ")
    

