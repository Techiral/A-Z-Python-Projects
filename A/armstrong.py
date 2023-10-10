num = int(input("Enter a number: "))
sum = 0

temp = num

if ( num <= 999):
   while temp > 0:
      digit = temp % 10
      sum  += digit ** 3
      temp //= 10
   if num == sum:
      print(num,"is an Armstrong number")
   else:
      print(num,"is not an Armstrong number")

elif ( (num > 999) and (num < 10000)):
   while temp > 0:
      digit = temp % 10
      sum += digit ** 4
      temp //= 10
   if num == sum:
      print(num,"is an Armstrong number")
   else:
      print(num,"is not an Armstrong number")

else:
   print(num,"is not an Armstrong number")

