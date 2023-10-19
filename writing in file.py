# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:14:36 2022

@author: Shantanu Durgvanshi
"""

myfile = open(r"D:\Study\OTHER\test.txt","a")
stry = " "
while stry:
 k = input("enter text here...(enter nnn for exit)")
 if k=="nnn":
     break
 else:
     s = myfile.write(k)
print(s)
myfile.close()