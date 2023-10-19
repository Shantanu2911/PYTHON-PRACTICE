# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:19:51 2021

@author: Shantanu Durgvanshi
"""

import random
    
a='''Nature includes living and nonliving components that together make 
life on Earth possible Some forms of nature can be seen through the lush
 green forests the vast sky above us the oceans without an end the mountains
 standing tall and so on Nature nourishes the survival needs of plants 
 animals and humans alike It provides the essential components of oxygen
 sunlight soil and water Health is the biggest wealth for a human being in 
 his her entire lifetime One can survive without excess money but survive 
 without good health Health is something that we buy with money 
 but we can take care of it and we can cure it when needed with the help of 
 the money If a person is not having good health he will not be able to 
 enjoy his her life to the fullest Money does make a person rich and happy
 but good health does Moreover a person can feel complete and happy
 without good health'''

a="".join(a).split()
x=random.choice(a)
x=list(x)
y=x.copy()
for i in range(0,len(y)):
    y[i]='?'
lives=9

while lives>=1 and ('?' in y):
    print(y)
    print("💖 "*lives)
    k=input("guess the letter or the whole word: ")

    if k in x:
        l=x.index(k)
        y[l]=k

    elif list(k)==x.copy():
        y=list(k).copy()

    else:
        lives-=1

if '?' not in y:
    print(x)
    print("YOU WIN!!!")

else:
    print("you losed...the correct word was...")
    print(x)