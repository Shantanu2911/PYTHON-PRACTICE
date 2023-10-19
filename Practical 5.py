#Practical 5: Solve a system of Homogeneous Equation using Gauss Jordan Method.
#using numpy

#Taking Input of Matrix From User (User Define matrix Input)
#NR : no. of rows
#NC : no. of columns

from numpy import matrix, linalg
import numpy as np

#Coefficient matrix(A) Elements
print("Enter the dimension of coefficient matrix (A): ")
NR = int(input("Enter the total number of rows: "))
NC = int(input("Enter the total number of columns: "))
print("Enter the elements of coefficients matrix (A) in a single line (seperated by spaces): ")
Coefficient_Entries = list(map(float, input().split()))
Coefficient_matrix = np.array(Coefficient_Entries).reshape(NR,NC)
print("Coefficient matrix is as follows: ",'\n',Coefficient_matrix,'\n')

#Column matrix (B) elements
print("Enter the elements of column matrix (B) in a single line (seperated by spaces): ")
Column_Entries = list(map(float, input().split()))
Column_matrix = np.array(Column_Entries).reshape(NR,1)
print("Column matrix is as follows: ",'\n',Column_matrix,'\n')

#Solution of Homogenous System of Equations using Gauss Jordan
Inv_of_Coefficient_Matrix = linalg.inv(Coefficient_matrix)
Solution_of_the_system_of_Equations = np.matmul(Inv_of_Coefficient_Matrix,Column_matrix)
print("Solution of the system of Equations using Gauss jordan")
print(Solution_of_the_system_of_Equations)
