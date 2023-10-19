# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 13:00:20 2022

@author: Shantanu Durgvanshi
"""

import random

numbers = list("0123456789")
alpha = list("abcdefghijklmnopqrstuvwxyz")
alpha_2 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
spc_symbol = list("@#$*(){}[]/")
x=[numbers,alpha,spc_symbol,alpha_2]
pwd=""
for i in range(9):    
  v=random.choice(x)
  c=random.choice(v)
  pwd+=c
print(pwd)