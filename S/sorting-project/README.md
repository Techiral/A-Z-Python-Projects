# Sorting Project

## Description

This project is a collection of sorting algorithms implemented in Python to visualize their sorting process. The goal is to implement four sorting algorithms and compare their performance, time complexity and how they scale with the size of the input.

## Algorithms

The algorithms implemented with their respective time complexity are:

- Bubble Sort O(n^2)
- Insertion Sort O(n^2)
- Merge Sort O(n log n)
- Selection Sort O(n^2)

## Structure

The project is structured as follows:

- `merge.py`: contains the implementation of the merge sort algorithm
- `bubble.py`: contains the implementation of the bubble sort algorithm
- `insertion.py`: contains the implementation of the insertion sort algorithm
- `selection.py`: contains the implementation of the selection sort algorithm
- `app.py`: contains the main function that runs the program

## How to use

1. To run the program, you need to have Python 3 installed. Then, you can run the following command:

```bash
python3 app.py
```

2. The program will ask you to enter the array that you want to sort. You can enter the array as a list of numbers separated by a space. For example:

```bash
Insert numbers separated by a space:
7 56 3 2 7 54
```

3. The program will ask you to enter the algorithm that you want to use to sort the array. You can enter the algorithm as a number between 1 and 4. For example:

```bash
Select the sorting method:
1.-Bubble Sort
2.-Insertion Sort
3.-Merge Sort
4.-Selection Sort
5.-Exit
4
```

4. The program will show you the sorted array and the number of steps that the algorithm took to sort the array. For example:

```bash
Original list: [7, 56, 3, 2, 7, 54]
Selection Sort Step 1: [2, 56, 3, 7, 7, 54]
Selection Sort Step 2: [2, 3, 56, 7, 7, 54]
Selection Sort Step 3: [2, 3, 7, 56, 7, 54]
Selection Sort Step 4: [2, 3, 7, 7, 56, 54]
Selection Sort Step 5: [2, 3, 7, 7, 54, 56]
Selection Sort Step 6: [2, 3, 7, 7, 54, 56]
Sorted list: [2, 3, 7, 7, 54, 56]
```

5. The program will ask you if you want to sort another array. If you enter `1`, the program will start again. If you enter `2`, the program will exit. For example:

```bash
Do you want to continue sorting?
1.-Yes
2.-No
1
```

6. The program will ask you if you want to continue with the same array or enter a new one. If you enter `1`, the program will start again. If you enter `2`, the program will ask you to enter a new array. For example:

```bash
Do you want to continue with the same list?
1.-Yes
2.-No
1
```

7. If you enter `2`, the program will ask you to enter a new array.

8. The program will start again until you enter `2` in step 5 or `5` in step 3 or if you enter a non valid option.