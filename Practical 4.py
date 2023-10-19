#Practical 4: Solve a system of Homogeneous Equation using Gauss Elimination Method.
#using numpy

#Taking Input of Matrix From User (User Define matrix Input)
#NR : no. of rows
#NC : no. of columns

import numpy as np

#coefficient matrix(A) Elements
print("Enter the dimension of coefficient matrix (A): ")
NR = int(input("Enter the total number of rows: "))
NC = int(input("Enter the total number of columns: "))
print("Enter the elements of coefficients matrix (A) in a single line (seperated by spaces): ")
Coefficient_Entries = list(map(float, input().split()))
Coefficient_matrix = np.array(Coefficient_Entries).reshape(NR,NC)
print("Coefficient matrix is as follows: ",'\n',Coefficient_matrix,'\n')

#column matrix (B) elements
print("Enter the elements of column matrix (B) in a single line (seperated by spaces): ")
Column_Entries = list(map(float, input().split()))
Column_matrix = np.array(Column_Entries).reshape(NR,1)
print("Column matrix is as follows: ",'\n',Column_matrix,'\n')

#Solution of Homogenous System of Equation using Gauss elimination Method
Solution = np.linalg.solve(Coefficient_matrix,Column_matrix)
print("Solution of the system of Equations using Gauss Elimination Method: ")
print(Solution)

