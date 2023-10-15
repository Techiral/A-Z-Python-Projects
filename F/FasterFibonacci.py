import sys
import math
#Fibonacci sequence

#Recursive "naive" approach
#Time Complexity: O(phi^n)
def recursive_fib(n):
    if n <= 1:
        return n
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

#dynamic programming/iterative approach
#Time Complexity: O(n)
def dynamic_fib(n,a=0,b=1):
    if n == 0:
        return a
    else:
        return dynamic_fib(n-1,b,a+b)

#Matrix Exponent approach
#Time Complexity: O(log(n))
def power_fib(n):
            if n <= 1:
                return n
            else:
                a, b, c, d, t = 0, 1, 1, 0, 0
                while n > 0:
                    if n % 2 == 1:
                        t = d * b + c * a
                        a = d * a + c * b + c * a
                        b = t
                    t = d * d + c * c
                    c = 2 * d * c + c * c
                    d = t
                    n = n // 2
                return a
#Doubling approach
#Time Complexity: still O(log(n)), for some reason it's slower than the matrix exponent approach (0.7s vs 1.1s on my machine)
def doubling_fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = doubling_fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)

n=1000000
sys.set_int_max_str_digits(max(700,math.ceil(1.3*n*math.log10((1+math.sqrt(5))/2))))
print(power_fib(n))
