# Attendance Tracker

This Python script allows you to track attendance for various dates. You can record the names of students present on a specific date, view attendance for a particular date, and save/load attendance data to/from a file. It's a simple tool designed to help you manage attendance records effortlessly.

## How to Use

1. **Take Attendance:** Record attendance for a specific date by entering the date (in the format `YYYY-MM-DD`) and the names of present students (comma-separated).

2. **View Attendance:** View attendance for a particular date by providing the date. The script will display the names of students present on that date.

3. **Save Attendance to File:** Save the attendance data to a file named `attendance.txt`. This file will store the recorded attendance records.

4. **Load Attendance from File:** Load attendance data from the `attendance.txt` file if it exists. This allows you to continue tracking attendance from where you left off.

5. **Exit:** Exit the attendance tracker.

## Code Overview

The script uses a dictionary called `attendance` to store attendance data. Each date maps to a list of present students.

The menu allows you to choose options by entering a number. You can take attendance, view attendance, save it to a file, or load it from a file. To exit the program, enter `5`.

## Example

```shell
Attendance Tracker Menu:
1. Take Attendance
2. View Attendance
3. Save Attendance to File
4. Load Attendance from File
5. Exit

Enter your choice: 1
Enter the date (YYYY-MM-DD): 2023-10-25
Enter the names of present students (comma-separated): Alice, Bob, Charlie
Attendance saved for 2023-10-25

Attendance Tracker Menu:
1. Take Attendance
2. View Attendance
3. Save Attendance to File
4. Load Attendance from File
5. Exit

Enter your choice: 2
Enter the date to view attendance: 2023-10-25
Attendance for 2023-10-25: Alice, Bob, Charlie

... (other menu options) ...
```

## Data Storage

The attendance data is stored in a file called `attendance.txt`. Each line in the file represents attendance for a specific date.

Example file content:

```plaintext
2023-10-25: Alice, Bob, Charlie
2023-10-26: Dave, Eve, Frank
```

## To-Do

- [ ] Add more features or data validation as needed.

Feel free to use and modify this code to suit your needs. Enjoy using the Attendance Tracker!