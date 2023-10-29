import os
import datetime

# Create a directory to store journal entries
if not os.path.exists('journal_entries'):
    os.mkdir('journal_entries')

def write_journal_entry():
    entry_date = input("Enter the date for your journal entry (YYYY-MM-DD): ")
    entry_text = input("Write your journal entry: ")
    
    entry_filename = f'journal_entries/{entry_date}.txt'
    
    with open(entry_filename, 'w') as file:
        file.write(entry_text)

def read_journal_entry():
    entry_date = input("Enter the date of the journal entry you want to read (YYYY-MM-DD): ")
    entry_filename = f'journal_entries/{entry_date}.txt'
    
    if os.path.exists(entry_filename):
        with open(entry_filename, 'r') as file:
            entry_text = file.read()
            print(f"Journal Entry for {entry_date}:\n{entry_text}")
    else:
        print(f"No journal entry found for {entry_date}.")

def main():
    while True:
        print("\nJournaling App Menu:")
        print("1. Write a new journal entry")
        print("2. Read a journal entry")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            write_journal_entry()
        elif choice == '2':
            read_journal_entry()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
