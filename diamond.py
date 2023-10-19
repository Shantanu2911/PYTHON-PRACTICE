# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:28:17 2021

@author: Shantanu Durgvanshi
"""

o=int(input("enter the width: "))
for i in range(o):
    print(" "*((o*2)-i),"* "*i)
for i in range(o,0,-1):
        print(" "*((o*2)-i),"* "*i)