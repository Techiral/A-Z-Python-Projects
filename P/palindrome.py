def palindrome_check_string(a):
    n = len(a)
    x = ""
    for i in range(n):
        x = x+ a[n-i-1]
    if (x == a):
        print("It is a Palindrome!!")
    else:
        print("It is not a Palindrome")    

def palindrome_check_int(a):
    n = int(a)
    ans = 0
    while (n != 0):
        digit = n%10
        ans = ans * 10 + digit
        n = n // 10
    if ( ans == int(a)) :
        print("palindrome!")
    else:
        print("Not Palindrome!")  


# main function starts from here!!
user_choice = int(input("On which of the following DATA TYPES would you like to perform check: \n 1. String \n 2. Integer \n"))

if (user_choice == 1):
    user_input_string = input("Enter a string to check if its palindrome  \n")
    palindrome_check_string(user_input_string)

elif (user_choice == 2):
    user_input_int = input("Enter a Integer to check if its palindrome  \n")
    palindrome_check_int(user_input_int);

else:
    print("Invalid Input")