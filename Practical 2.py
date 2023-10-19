#Practical 2: Generate the matrix into echelon form and find its rank.
#taking input of matrix from user (User define Matrix Input)
#NR: Number of rows
#NC: Number of columns

import numpy as np
NR = int(input("Enter The Number Of Rows : "))
NC = int(input("Enter The Number Of Columns : "))

print("Enter the enteries in a single line(seperated by spaces): ")

#user input of enteries in a
#single line seperated by space
enteries = list(map(int,input().split()))

#For printing the matrix
matrix = np.array(enteries).reshape(NR,NC)
print("Matrix X is as follows:",'\n',matrix)

#For finding the Rank of a Matrix
print("The rank of a matrix is:",np.linalg.matrix_rank(matrix))
