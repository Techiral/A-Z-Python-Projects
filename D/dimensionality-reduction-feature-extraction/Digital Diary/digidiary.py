import os
from datetime import datetime

def write_diary_entry():
    entry_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry_text = input("Write your diary entry: ")

    with open("diary.txt", "a") as diary_file:
        diary_file.write(f"{entry_date}:\n{entry_text}\n\n")
    print("Diary entry added successfully!")

def read_diary_entries():
    if not os.path.exists("diary.txt"):
        print("No diary entries found.")
    else:
        with open("diary.txt", "r") as diary_file:
            diary_entries = diary_file.read()
            print(diary_entries)

if __name__ == "__main__":
    while True:
        print("\nDigital Diary Menu:")
        print("1. Write Diary Entry")
        print("2. Read Diary Entries")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            write_diary_entry()
        elif choice == "2":
            read_diary_entries()
        elif choice == "3":
            print("Exiting Digital Diary. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
