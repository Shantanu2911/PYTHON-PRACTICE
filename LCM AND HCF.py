# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:51:09 2021

@author: Shantanu Durgvanshi
"""

a=int(input("enter a number: "))
b=int(input("enter a number: "))
for i in range(1,a):
    if(a%i==0 and b%i==0):
        hcf=i
lcm=a*b/hcf
print("HCF:",hcf)
print("LCM:",lcm)