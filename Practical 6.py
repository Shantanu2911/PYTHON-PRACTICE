#Practical 6: Python Example to find null space and nullity of a matrix
#Sympy is a library in python
#
import numpy as np
from sympy import Matrix

#Coefficient Matrix(A) Elements
print("Enter the dimension of coefficient matrix (A): ")
NR = int(input("Enter the total number of rows: "))
NC = int(input("Enter the total number of columns: "))
print("Enter the elements of coefficients matrix (A) in a single line (seperated by spaces): ")
Entries = list(map(float, input().split()))
A = np.array(Entries).reshape(NR,NC)
print("Matrix (A) is as follows: ",'\n', A,"\n")

#Matrix A
A = Matrix(A)
#Null Space of A
Nullspace = A.nullspace() #Here Nullspace is a list
Nullspace = Matrix(Nullspace) #Here Nullspace is a Matrix
print("Null Space of a matrix (A) is =",Nullspace,'\n')
