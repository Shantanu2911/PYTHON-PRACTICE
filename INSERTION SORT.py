# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 20:30:33 2021

@author: Shantanu Durgvanshi
"""

a=[1,5,3,2,4]
k=a.copy()
n=len(k)
for i in range(1,n):
    key=k[i]
    while(i-1)>=0 and key<k[i-1]:
        k[i]=k[i-1]
        i=i-1
    else:
        k[i]=key
print("original list:",a)
print("sorted list:  ",k)