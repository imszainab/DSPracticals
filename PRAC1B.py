'''Practical 1 (b)Write a program to perform the Matrix addition, Multiplication and Transpose
Operation.'''
Matrix1 = [[3, 4, -6], 
      [12,71,24], 
      [21,3,21]]

Matrix2 = [[2, 16, -16],
           [1,7,-3], 
           [-1,3,3]]
Matrix3 = [[0,0,0,],
     [0,0,0,],
     [0,0,0,]]

# Matrix Addition
for i in range(len(Matrix1)):
    for j in range(len(Matrix2[0])):
        for k in range(len(Matrix2)):
            Matrix3[i][j] += Matrix1[i][k] + Matrix2[k][j]
        
print(Matrix3)

# Matrix Multiplication

Matrix3 = [[0, 0, 0, 0], 
        [0, 0, 0, 0], 
        [0, 0, 0, 0]] 

for i in range(len(Matrix1)):
    for j in range(len(Matrix2[0])):
        for k in range(len(Matrix2)):
            Matrix3[i][j] += Matrix1[i][k] * Matrix2[k][j]
        
print(Matrix3)

#matrix transpose
for i in map(list, zip(*Matrix1)):
    print(i)
