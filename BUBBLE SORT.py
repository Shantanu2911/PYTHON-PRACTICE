# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 20:19:07 2021

@author: Shantanu Durgvanshi
"""

a=[1,5,3,2,4]
l=a.copy()
n=len(l)
for i in range(0,n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
r=sorted(l,reverse=True)
print("\t Oringinal list:  ",a)
print("\t Sorted list:     ",l)
print("\t Reversed list:   ",l)