import numpy as np
 
rows = 3
col = 3

X = np.zeros((rows,col), dtype=int)
Y = np.zeros((rows,col), dtype=int)

def inpMatrix(matrix,rows,col):
    for i in range (rows):
        for j in range(col):
            matrix[i,j] = int(input(f"Enter element for row{i+1}, column{j+1}: "))
    print(f"Element for matrix: \n {matrix}")

inpMatrix(X,rows,col)
inpMatrix(Y,rows,col)

print("\n")

result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
print("The result is : \n")
for r in result:
   print(r)
