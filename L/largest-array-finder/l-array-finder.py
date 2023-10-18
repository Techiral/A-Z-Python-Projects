# Python3 program to find maximum
# in arr[] of size n
 
def largest(arr, n):
 
    # Sort the array
    arr.sort()
 
    # The last element of the
    # array is the largest element
    return arr[n-1]
    # or return arr[-1]
 
# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)
