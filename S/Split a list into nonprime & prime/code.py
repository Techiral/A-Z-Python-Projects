# Get the size of the list1 from the user
n = int(input("Enter the size of the list1: "))

# Initialize lists for prime and non-prime numbers
prime_list = []
non_prime_list = []

# Prompt the user to enter numbers
print("Enter the numbers:")
for i in range(n):
    e = int(input())
    f = 0  # Reset the factor count for each number

    # Check if the number is prime or non-prime
    for j in range(2, e):
        if e % j == 0:
            f += 1
            break  # No need to continue checking, it's not prime
    if f == 0:
        prime_list.append(e)
    else:
        non_prime_list.append(e)

# Print the prime numbers
print("Prime numbers list:")
print(prime_list)

# Print the non-prime numbers
print("Non-prime numbers list:")
print(non_prime_list)
