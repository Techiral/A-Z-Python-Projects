from bubble import BubbleSort
from insertion import InsertionSort
from selection import SelectionSort
from merge import MergeSort

def sorting(nums: list[int], op: int) -> None:
  # Print the original list
  print("Original list:", nums)
  # Mapping of sorting algorithms to their respective classes
  sorting_algorithms = {
    1: BubbleSort,
    2: InsertionSort,
    3: MergeSort,
    4: SelectionSort
  }

  # Create an instance of the chosen sorting algorithm
  sort_obj = sorting_algorithms[op](nums.copy())
  # Perform the sorting and print the result
  result_sort = sort_obj.sort()
  print("Sorted list:", result_sort)

def logic(nums: list[int]) -> None:
  while True:
    message = False
    # Choose a sorting algorithm
    op = int(input("Select the sorting method:\n1.-Bubble Sort\n2.-Insertion Sort\n3.-Merge Sort\n4.-Selection Sort\n5.-Exit\n"))
    if 1 <= op <= 4:
      sorting(nums, op)
      # Ask if the user wants to continue sorting
      op = int(input("Do you want to continue sorting?\n1.-Yes\n2.-No\n"))
      if op == 1:
        # Ask if the user wants to continue with the same list or enter a new one
        op = int(input("Do you want to continue with the same list?\n1.-Yes\n2.-No\n"))
        if op == 1:
          continue
        elif op == 2:
          # Enter a new list
          nums = list(map(int, input("Insert numbers separated by spaces:\n").split()))
          continue
        else:
          message = True
    else:
      if op != 5:
        message = True

    if message:
        print("Invalid option")
    break

def main():
  try:
    # Enter the initial list
    nums = list(map(int, input("Insert numbers separated by spaces:\n").split()))
    logic(nums)
  except ValueError:
    print("Invalid input. Make sure to enter only numbers.")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()
