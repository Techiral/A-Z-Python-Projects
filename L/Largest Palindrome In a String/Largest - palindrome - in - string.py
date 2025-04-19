def largest_pallindrome(s):
    largest = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j]==s[i:j][::-1] and len(s[i:j]) > len(largest):
                largest = s[i:j]
    return largest

string = input("Enter a string: ")
print("The largest palindrome in the string is: ", largest_pallindrome(string))
