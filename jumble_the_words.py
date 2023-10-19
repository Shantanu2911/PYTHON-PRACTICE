# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:17:06 2021

@author: Shantanu Durgvanshi
"""

import random

a="""computing 
machine 
calculator 
programmer 
hardware 
laptop 
mainframe 
server 
peripheral 
electronics 
analog computer 
central processing unit 
personal computer  
imac 
computer science 
microprocessor 
internet 
information 
machine code 
vacuum tube 
computer program 
software 
keyboard 
supercomputer 
memory 
computer programming 
integrated circuit 
desktop 
floppy disk 
processor 
monitor 
turing machine 
charles babbage 
machines 
astrolabe 
abacus 
home computer 
cyber 
ibook 
computer hardware 
slide rule 
automation 
digital 
computation 
antivirus 
macintosh 
turing-complete 
transistor 
arithmetic 
compiler 
laptop computer  
predictor 
data 
digital communication 
digital computer 
data converter  
control flow 
diskette 
mechanical computer 
james thomson 
visual display unit 
number cruncher 
chip 
computer circuit 
expansion slot 
information
peripheral device 
input device 
beta test 
alpha test 
computer memory 
antikythera mechanism 
estimator 
figurer 
reckoner 
files 
bios 
computer 
loom 
laptop computers 
minicomputer 
desktop computers 
microcomputer 
information processing system 
electronic computer 
boolean logic 
data processor 
laptops 
spyware 
handheld device 
antivirus software 
hackers 
scratchpad 
workstations 
notebook computers 
windows
graphics 
desktops 
supercomputers 
wire 
techie 
world
printer 
digital data 
softwares 
desktop 
handheld 
embedded system 
servers 
copier 
excel spreadsheet 
intel 
reformat 
desktop computer 
palm pilot 
washing machine 
spreadsheets 
business 
floppy 
compute 
compatible 
console 
format 
formatting 
website 
client 
node 
pornographic images 
module """
a="".join(a).split()
x=random.choice(a)
x=list(x)
y=x.copy()
l=len(y)
key=int(l/2-1)
for i in range(0,l):
        if i%key==0 and i<(l-key):
            y[i],y[i+key]=y[i+key],y[i]
print(y)
s=input("unscrammble the word: ")
while list(s)!=x.copy(): 
 s=input("unscrammble the word or just say (i quit): ")
 if s=="i quit":
     print("<<<YOU LOSE>>>")
     print("the correct word was...",x)
     break
else:
 print("IT'S ABSOLUTELY RIGHT...")
 print("you won !!!")