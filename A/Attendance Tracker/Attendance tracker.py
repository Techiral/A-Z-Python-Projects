# Initialize an empty attendance dictionary
attendance = {}

def take_attendance():
    date = input("Enter the date (YYYY-MM-DD): ")
    present_students = input("Enter the names of present students (comma-separated): ").split(',')
    
    # Update attendance for the given date
    attendance[date] = present_students

def view_attendance():
    date = input("Enter the date to view attendance: ")
    if date in attendance:
        present_students = attendance[date]
        print(f"Attendance for {date}: {', '.join(present_students)}")
    else:
        print("Attendance not taken for this date.")

def save_attendance_to_file():
    with open("attendance.txt", "w") as file:
        for date, students in attendance.items():
            file.write(f"{date}: {', '.join(students)}\n")
        print("Attendance saved to 'attendance.txt'")

def load_attendance_from_file():
    try:
        with open("attendance.txt", "r") as file:
            for line in file:
                date, students_str = line.strip().split(": ")
                students = students_str.split(', ')
                attendance[date] = students
    except FileNotFoundError:
        print("No attendance data found.")

while True:
    print("\nAttendance Tracker Menu:")
    print("1. Take Attendance")
    print("2. View Attendance")
    print("3. Save Attendance to File")
    print("4. Load Attendance from File")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        take_attendance()
    elif choice == "2":
        view_attendance()
    elif choice == "3":
        save_attendance_to_file()
    elif choice == "4":
        load_attendance_from_file()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
