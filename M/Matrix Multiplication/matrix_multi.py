
X = [[8,7,3],
    [4 ,6,6],
    [5,10,9]]
Y = [[8,8,1,2],
    [6,10,3,5],
    [8,5,9,1]]
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)
