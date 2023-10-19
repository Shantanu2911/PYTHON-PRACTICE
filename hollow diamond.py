# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:38:22 2021

@author: Shantanu Durgvanshi
"""

n=int(input("ENTER the no. of rows: "))
if n%2==0:
    s1=s2=n/2
    for i in range(n):
        for j in range(n):
           if j==s1 or j==s2:
               print("*",end="")
           else:
                print(end=" ")
        print()
        if i < n/2 and i!=(n/2)-1:
            s1-=1
            s2+=1
        elif i==(n/2)-1:
            i+=1
        else:
            s1+=1
            s2-=1
else:
    s1=s2=int(n/2)
    for i in range(n):
        for j in range(n):
           if j==s1 or j==s2:
               print("*",end="")
           else:
                print(end=" ")
        print()
        if i < int(n/2):
            s1-=1
            s2+=1
        else:
            s1+=1
            s2-=1