# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:09:33 2021

@author: Shantanu Durgvanshi
"""

a=input("enter your name: ")
a+=" "
l=len(a)
c=0
print(a)
for i in range(0,l):
    if a[i]==" ":
        c+=1
s=0
for i in range(0,l):
    if(a[i]==" "):
        x=((i-s)//2)
        print(a[s+x])
        s=i+1
        
        