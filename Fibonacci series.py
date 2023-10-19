# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 12:39:42 2021

@author: Shantanu Durgvanshi
"""

# num=int(input("enter a number: "))
# s=0
# a=1
# for a in range(num+1):
#     s+=a
#     print("0+",s)


# num=int(input("enter a number: "))
# temp=num
# s=0
# for a in range(0,num):
#     while temp>0:
#         print(a,",",a+s,end="")
#         s+=a
#         temp-=1

num=int(input("enter a number: "))
first=0
second=1
print("\nthe fibonacci series is:->")
print("0,1",end=",")
for i in range(2,num):
    nxt=first+second
    print(nxt,end=",")
    first=second
    second=nxt
print("\b ")