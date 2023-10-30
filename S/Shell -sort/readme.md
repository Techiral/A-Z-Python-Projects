# Shell Sort in Python

This is a Python implementation of the Shell Sort algorithm. Shell Sort is an efficient sorting algorithm that improves upon the Insertion Sort by sorting elements at a larger distance first and then gradually reducing the gap until the entire array is sorted.

## Getting Started

### Prerequisites

- Python 3.x

### Usage

1. Clone the repository or download the `shell_sort.py` file.

2. Use the `shell_sort` function to sort your list. For example:

    ```python
    arr = [12, 34, 54, 2, 3]
    shell_sort(arr)
    print("Sorted array is:", arr)
    ```

3. Replace `arr` with your own list to sort.

## Algorithm

The Shell Sort algorithm works as follows:

1. Divide the input list into smaller sublists by selecting a gap size (usually half the length of the list) and comparing elements that are this gap apart.

2. Perform Insertion Sort on each sublist.

3. Gradually reduce the gap size and repeat the process until the gap size becomes 1.

4. The final pass with a gap size of 1 performs a regular Insertion Sort and fully sorts the list.

## License

This project is licensed under the MIT License

## Acknowledgments

- The Shell Sort algorithm is attributed to Donald Shell, who introduced the idea of diminishing increment sorting in 1959.

## Authors

- EmojiSMAH

Feel free to add your name and any additional information you find relevant to your specific implementation.

## Contributing

If you'd like to contribute to this project or suggest improvements, please open an issue or create a pull request.

