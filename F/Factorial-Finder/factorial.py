
# Function for returning factorial of 'n' using RECURSION
def fact(n):
  if(n==1):
    return 1
  else:
    return n*fact(n-1)

print("Enter a number of your choice : ")
Num = int(input())
result=fact(Num)
print("Factorial of ",Num," : ",result)
