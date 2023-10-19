"""
    This function implements the binary search algorithm to find the index of the target element in the given sorted array.

    Parameters:
    arr (list): A sorted list of elements to be searched.
    target: The element to be found in the list.

    Returns:
    int: Index of the target in the array if it exists, otherwise -1.
    """
def binary_search(arr, target):
    
    left, right = 0, len(arr) - 1  # Initialize the left and right pointers

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        if arr[mid] == target:  # Check if the middle element is the target
            return mid
        elif arr[mid] < target:  # If the target is greater, ignore the left half
            left = mid + 1
        else:  # If the target is smaller, ignore the right half
            right = mid - 1

    return -1  # Return -1 if the target is not found


# Example case
arr = [2, 3, 4, 10, 40] 
target = 10
result = binary_search(arr, target)

if result != -1:
    print(f"Element is present at index {result}.")
else:
    print("Element is not present in array.")
