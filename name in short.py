# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:54:46 2021

@author: Shantanu Durgvanshi
"""
a=input("enter your name: ")
l=len(a)
for i in range(0,l):
    if a[i]==" ":
        print(a[0],a[(i-1)],a[i+1],a[l-1])