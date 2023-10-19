# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 21:37:05 2022

@author: Shantanu Durgvanshi
"""

n = int(input('range 1-9999\nenter a number: '))
r=""
a = str(n)
l = len(a)
if a!="0":
 if l<5:
  if l<4:
     if l==3:
         a = "0" + a
     if l==2:
         a = "00" + a
     if l==1:
         a = "000" + a
  l = len(a)
  for i in range(1):
    if int(a[0])<5 and int(a[0])!=4:
        r+="M"*(int(a[0]))
    if int(a[0])==4:
        r+="(IV)"
        print("brackets represent bar")
    if int(a[0])>=5 and int(a[0])<9:
        r+="(V"+("I"*(int(a[0])-5))+")"
        print("brackets represent bar")
    if int(a[0])==9:
        r+="(IX)"
        print("brackets represent bar")

  for i in range(1):
    if int(a[1])<5 and int(a[1])!=4:
        r+="C"*(int(a[1]))
    if int(a[1])==4:
        r+="CD"
    if int(a[1])>=5 and int(a[1])<9:
        r+="D"+("C"*(int(a[1])-5))
    if int(a[1])==9:
        r+="CM"
        
  for i in range(1):
    if int(a[2])<5 and int(a[2])!=4:
        r+="X"*(int(a[2]))
    if int(a[2])==4:
        r+="XL"
    if int(a[2])>=5 and int(a[2])<9:
        r+="L"+("X"*(int(a[2])-5))
    if int(a[2])==9:
        r+="XC"

  for i in range(1):
    if int(a[3])<5 and int(a[3])!=4:
        r+="I"*(int(a[3]))
    if int(a[3])==4:
        r+="IV"
    if int(a[3])>=5 and int(a[3])<9:
        r+="V"+("I"*(int(a[3])-5))
    if int(a[3])==9:
        r+="IX"
 else:
     print("smaller number plzz...")
if a=="0":
 print("no value for it...")    
print(r)