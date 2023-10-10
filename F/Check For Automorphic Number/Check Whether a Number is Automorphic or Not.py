# Automorphic Number 

num = int(input("Enter a number : "))
length = len(str(num))
sqr = str(num ** 2)
print(sqr)

new = int(sqr[(length):])
print(new)

if (new == num):
    print("It is an Automorphic Number")
else:
    print("It is not an Automorphic Number")


