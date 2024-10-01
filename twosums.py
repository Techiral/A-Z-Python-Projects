import numpy as np

nums = np.zeros((5),dtype=int)

for i in range(5):
    nums[i]=input("Enter 5 values: ")

print(nums)
flag = 0

target = int(input("Enter the target: "))

for i in range(5):
    for j in range(i+1,5):
        if(nums[i]+nums[j]== target):
            print( {i , j})
            flag = 1
        
if ( flag == 0):
    print("No Possible Combnination available! ")
