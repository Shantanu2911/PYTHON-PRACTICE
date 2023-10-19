# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 23:14:42 2021

@author: Shantanu Durgvanshi
"""

a=[7,4,9,23,0]
print("ORIGINAL LIST IS:",a)
n=len(a)
for i in range(n):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        else:
            j+=1
print("SORTED LIST IS:",a)

print()
print("/////////////////////////////////")
print()

a=[2,8,1,5,0,9,4,2,65,0,23]
print("original list is:",a)
n=len(a)
for i in range(1,n):
    key=a[i]
    j=i-1
    while j>=0 and key<a[j]:
        a[j+1]=a[j]
        j-=1
    else:
        a[j+1]=key
print("sorted list is",a)
    
