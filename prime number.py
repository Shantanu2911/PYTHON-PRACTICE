# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:55:02 2022

@author: Shantanu Durgvanshi
"""

# a = int(input("enter a number: "))
# for i in range(2,a):
#     if a%i==0:
#         count=1
# if count == 1:
#     print(a,"is composite")
# elif count != 1:
#     print(a,"is prime")

for j in range(1,100):
 for i in range(2,j):
    if j%i==0:
        i+=1
        break
 else:
        print(j)
