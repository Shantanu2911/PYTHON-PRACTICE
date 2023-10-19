# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:03:40 2021

@author: Shantanu Durgvanshi
"""

x=int(input("ENTER THE VALUE OF X: "))
n=int(input("ENTER THE VALUE OF N: "))
s=0
for a in range(1,n+1):
    if a%2==0:
        fact=1
        for b in range(1,a+1):
            fact=fact*b
        num=x**a/fact
        s+=num
    elif a==1:
        s+=x
    else:
        fac=1
        for c in range(1,a+1):
            fac=fac*c
        num=x**a/fac
        s-=num
print("the sum of the series is",s)