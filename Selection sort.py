def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Taking user input for the list
user_input = input("Enter elements of the list separated by space: ")
input_list = list(map(int, user_input.split()))

# Sorting the user input list using selection_sort function
selection_sort(input_list)

# Displaying the sorted list
print("Sorted Array:", input_list)
