# Python3 program to print all primes 
# between 1 to N in reverse order 
# using Sieve of Eratosthenes
def Reverseorder(n):

	# Create a boolean array "prime[0..n]" 
	# and initialize all entries it as true. 
	# A value in prime[i] will finally be 
	# false if i is Not a prime, else true.
	prime = [True] * (n + 1);

	p = 2; 
	while(p * p <= n):

		# If prime[p] is not changed, 
		# then it is a prime
		if (prime[p] == True): 

			# Update all multiples of p
			for i in range((p * 2), (n + 1), p):
				prime[i] = False;
		p += 1;

	# Print all prime numbers in 
	# reverse order
	for p in range(n, 1, -1):
		if (prime[p]):
			print(p, end = " ");

# Driver Code

# static input
N = 25;

# to display
print("Prime number in reverse order");

if (N == 1):
	print("No prime no exist in this range");
else:
	Reverseorder(N); # calling the function

# This code is contributed by mits
