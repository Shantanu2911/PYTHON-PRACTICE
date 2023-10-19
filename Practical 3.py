#Practical 3: Find Cofactors, Determinant, Adjoint And Inverse of a matrix #using numpy
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
A = np.array(enteries).reshape(NR,NC)
print("Matrix X is as follows:",'\n',A)

A_Inverse = np.linalg.inv(A)
Transpose_of_A_Inverse = np.transpose(A_Inverse)
Determinant_of_A = np.linalg.det(A)
Cofactor_of_A = np.dot(Transpose_of_A_Inverse,Determinant_of_A)

#For finding the cofactor of a matrix
print("The cofactor of a matrix is:",'\n',Cofactor_of_A)

#For finding the determinant of a matrix
print("The Determinant of a matrix is:",'\n',Determinant_of_A)

#For finding the Adjoint of a matrix
Adjoint_of_A = np.transpose(Cofactor_of_A)
print("The Adjoint of a matrix is:",'\n',Adjoint_of_A)
