#Practical 1: Create and transform vectors and matrices (the transpose vector (matrix) conjugate)
#transpose of a vector (matrix))

#Program to transpose a matrix
#using numpy

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

#For transposing the matrix
print("Transpose of matrix X is as follows:",'\n',np.transpose(matrix))
