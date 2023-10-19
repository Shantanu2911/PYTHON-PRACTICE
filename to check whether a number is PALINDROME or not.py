# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 11:43:21 2021

@author: Shantanu Durgvanshi
"""

num=int(input("enter a number: "))
num=str(num)
length=len(num)
if num[0:length]==num[::-1]:
    print("PALINDROME")  
else:      
    print("NOT A PALINDROME")