import random

def analyze_numbers(numbers):

    print("Original List:", numbers)

    sorted_numbers = sorted(numbers)
    print("Sorted List:", sorted_numbers)

    max_number = max(numbers)
    print("Maximum Number:", max_number)

    min_number = min(numbers)
    print("Minimum Number:", min_number)

    sum_of_numbers = sum(numbers)
    print("Sum of Numbers:", sum_of_numbers)

    average = sum_of_numbers / len(numbers)
    print("Average:", average)

numbers = [random.randint(1, 100) for _ in range(10)]

analyze_numbers(numbers)