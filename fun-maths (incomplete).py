# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 22:07:59 2022

@author: Shantanu Durgvanshi
"""

import random
import time

# a,b,c = random.choice(num),random.choice(num),random.choice(num)
# f=a*b
# print(a,"X",b,"=",end="")
# time.sleep(1)
# print("1...",end="")
# time.sleep(1)
# print("2...",end="")
# time.sleep(1)
# ans=int(input())
ans,f,s,d = 1,1,1,1
while ans==f:
    num = [0,1,2,3,4,5,6,7,8,9]
    a,b,c = random.choice(num),random.choice(num),random.choice(num)
    print(a,"X",b,"=",end="")
    for i in range(1,4):
        ans=int(input())
        if ans==a*b:
            print("You win round 1 !!!")
            break
        else:
            print(i,"...")
            time.sleep(1)
        

