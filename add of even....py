# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:03:10 2021

@author: Shantanu Durgvanshi
# """

sum=0
a=1
i=input("enter yes/no ")
j=0
while (i=="yes")and(j<5):
            a=int(input("enter number:"))
            if(a%2==0):
                sum=sum+a
                j+=1
            elif a==9211:
                print(sum)
                break
            else:
                print("enter again")
else:
    print(sum)
