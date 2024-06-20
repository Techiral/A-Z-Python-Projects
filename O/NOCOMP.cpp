# This python program tells if there exists a pair in array whose sum results in x.

# Function to find and print pair


def chkPair(A, size, x):
	for i in range(0, size - 1):
		for j in range(i + 1, size):
			if (A[i] + A[j] == x):
				return 1
	return 0


if __name__ == "__main__":
	A = [0, -1, 2, -3, 1]
	x = -2
	size = len(A)

	if (chkPair(A, size, x)):
		print("Yes")

	else:
		print("No")

	# This code is contributed by rakeshsahni
      // C++ program for the above approach
#include <bits/stdc++.h>

using namespace std;

// Function to find and print pair
bool chkPair(int A[], int size, int x)
{
	for (int i = 0; i < (size - 1); i++) {
		for (int j = (i + 1); j < size; j++) {
			if (A[i] + A[j] == x) {
				return 1;
			}
		}
	}

	return 0;
}

// Driver code
int main()
{
	int A[] = { 0, -1, 2, -3, 1 };
	int x = -2;
	int size = sizeof(A) / sizeof(A[0]);

	if (chkPair(A, size, x)) {
		cout << "Yes" << endl;
	}
	else {
		cout << "No" << x << endl;
	}

	return 0;
}

// This code is contributed by Samim Hossain Mondal.
