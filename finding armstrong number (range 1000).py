# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 19:03:40 2021

@author: Shantanu Durgvanshi
"""
for num in range(100,1000):
    a=num
    s=0
    while a>0:
        digit=a%10
        s+=digit**3
        a//=10
    if num==s:
        print(num,"is an armstrong number")
    else:
        num+=1