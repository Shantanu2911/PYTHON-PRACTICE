# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 22:56:16 2022

@author: Shantanu Durgvanshi
"""


a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
num=[]
if a>b: 
 for i in range(1,a):
    if a%i==0 and b%i==0:
        num.append(i)
    else:
        i+=1
 for j in range(1,a):
     if a%j==0:
         num.append(j)
     else:
        i+=1
elif b>a: 
 for i in range(1,b):
    if b%i==0 and a%i==0:
        num.append(i)
    else:
        i+=1
 for j in range(1,b):
     if b%j==0:
         num.append(j)
     else:
        i+=1
print(set(num))
