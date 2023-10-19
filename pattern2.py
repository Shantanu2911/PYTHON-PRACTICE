# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 21:23:01 2022

@author: Shantanu Durgvanshi
"""

'''
#
# #
#  #
#   #
#    #
#    #
 #   #
  #  #
   # #
    #
'''

for i in range(5):
 if i>0:
    print("#"+(" "*i)+"#")
 else:
    print("#"+(" "*i))
for i in range(5,0,-1):
 if i>1:
    print((" "*(5-i))+"#"+(" "*(i-1))+"#")
 else:
     print((" "*(5-i))+"#"+(" "*(i-1)))