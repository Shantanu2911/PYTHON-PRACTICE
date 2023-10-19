# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:57:45 2022

@author: Shantanu Durgvanshi
"""

n = int(input('enter a number (4 digit): '))
a = str(n)[::-1]
l = len(a)
temp=""
if a!="0":
 if l!=4:
    if l==3:
        a+="0"
    if l==2:
        a+="00"
    if l==1:
        a+="000"
 l=len(a)    
 for i in range(1):
    if a[3]=="1":
     temp+="one thousand"
    if a[3]=="2":
     temp+="two thousand"
    if a[3]=="3":
     temp+="three thousand"
    if a[3]=="4":
     temp+="four thousand"
    if a[3]=="5":
     temp+="five thousand"
    if a[3]=="6":
     temp+="six thousand"
    if a[3]=="7":
     temp+="seven thousand"
    if a[3]=="8":
     temp+="eight thousand"
    if a[3]=="9":
     temp+="nine thousand"
    if a[3]=="0":
     temp+=""
 temp+=" "
 for i in range(1):
    if a[2]=="1":
     temp+="one hundred"
    if a[2]=="2":
     temp+="two hundred"
    if a[2]=="3":
     temp+="three hundred"
    if a[2]=="4":
     temp+="four hundred"
    if a[2]=="5":
     temp+="five hundred"
    if a[2]=="6":
     temp+="six hundred"
    if a[2]=="7":
     temp+="seven hundred"
    if a[2]=="8":
     temp+="eight hundred"
    if a[2]=="9":
     temp+="nine hundred"
    if a[2]=="0":
     temp+=""
 temp+=" "
 for i in range(1):
     if a[1]=="1":
      if a[0]=="0":
          temp+="ten"
      if a[0]=="1":
          temp+="eleven"
      if a[0]=="2":
          temp+="twelve"
      if a[0]=="3":
          temp+="thirteen"
      if a[0]=="4":
          temp+="forteen"
      if a[0]=="5":
          temp+="fifteen"
      if a[0]=="6":
          temp+="sixteen"
      if a[0]=="7":
          temp+="seventeen"
      if a[0]=="8":
          temp+="eighteen"
      if a[0]=="9":
          temp+="ninteen"
     if a[1]=="2":
      temp+="twenty"
     if a[1]=="3":
      temp+="thirty"
     if a[1]=="4":
      temp+="forty"
     if a[1]=="5":
      temp+="fifty"
     if a[1]=="6":
      temp+="sixty"
     if a[1]=="7":
      temp+="seventy"
     if a[1]=="8":
      temp+="eighty"
     if a[1]=="9":
      temp+="ninty"
     if a[1]=="0":
      temp+=""
 temp+=" "
 for i in range(1):
     if a[0]=="1" and a[1]!="1":
      temp+="one"
     if a[0]=="2" and a[1]!="1":
      temp+="two"
     if a[0]=="3" and a[1]!="1":
      temp+="three"
     if a[0]=="4" and a[1]!="1":
      temp+="four"
     if a[0]=="5" and a[1]!="1":
      temp+="five"
     if a[0]=="6" and a[1]!="1":
      temp+="six"
     if a[0]=="7" and a[1]!="1":
      temp+="seven"
     if a[0]=="8" and a[1]!="1":
      temp+="eight"
     if a[0]=="9" and a[1]!="1":
      temp+="nine"
     if a[0]=="0" and a[1]!="1":
      temp+=""
 print(temp)
if a=="0":
    print("ZERO")
    