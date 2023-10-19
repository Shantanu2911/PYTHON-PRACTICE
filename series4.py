# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 09:23:13 2022

@author: Shantanu Durgvanshi
"""

""" s = (1) + (1+2) + (1+2+3) + ...."""

a = int(input("enter the range of numbers: "))
s=0
t=0
for i in range(a+1):
    s+=i
    t+=s
print("the sum is:",t)
