# Python program to 
# print Diamond shape 

# Function to print 
# Diamond shape 
def Diamond(rows): 
	n = 1
	for i in range(1, rows + 1): 
		# loop to print spaces 
		for j in range (1, (rows - i) + 1): 
			print(end = " ") 
		
		# loop to print star 
		while n != (i+1): 
			print("*", end = " ") 
			n = n + 1
		n = 1
		
		# line break 
		print() 

	k = 0
	n = 0
	for i in range(1, rows + 1): 
		# loop to print spaces 
		for j in range (1, k + 1): 
			print(end = " ") 
		k = k + 1
		
		# loop to print star 
		while n <= (rows - i): 
			print("*", end = " ") 
			n = n + 1
		n = 0
		print() 

# Driver Code 
# number of rows input 
rows = 5
Diamond(rows)
