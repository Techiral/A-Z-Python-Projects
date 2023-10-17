#This program will print number from  1 to 100
#if the number is divisible by 3 it will print "fizz" instead 
#if the number is divisible by 5 it will print 'buzz' instead 
#if divisible by both it will print fizzbuzz
print("****  PROGRAM FOR FIZZBUZZ PATTERN  *******")
for n in range(100) :
    if (n%3 == 0 and n%5!=0) :
        print("fizz")
    elif(n%5 == 0 and n%3!=0) :
        print("buzz") 
    elif (n%3 == 0 and n%5==0) :
        print("fizzbuzz")
    else : print(n)
 