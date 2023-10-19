# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 21:02:15 2022

@author: Shantanu Durgvanshi
"""

# def writelines():
#     file = open("D:\IDLE\.vscode\hello.txt","w")
#     a = input("type y to write more lines or type n to quit: ")
#     while a=="y":
#         b = input("enter the line you wanna write: ")
#         file.write(b)
#         a = input("type y to write more lines or type n to quit: ")
#         file.close()        
# writelines()

# import pickle
# ID = {1:"Ziva",2:"53050",3:"IT",4:"38",5:"Dunzo"}
# fin = open("Emp.pkl","wb")
# pickle.dump(ID,fin)
# fin.close()
# fout = open("Emp.pkl","rb")
# ID = pickle.load(fout)
# print(ID[5])

# import pickle
# List1 = ["Roza",{'a':23,"b":True},(1,2,3),[['dogs','cats'],None]]
# List2 = ["Rita",{'x':45,"y":False},(9,5,3),[['insects','bees'],None]]
# with open ('data.pkl','wb') as f:
#     f.write(List1)
# with open ('data.pkl','wb') as f:
#     f.write(List2)
# with open ('data.pkl','rb') as f:
#     List1 = pickle.load(f)
# print(List1)

# import csv
# with open("D:\IDLE\.vscode\data.csv","r+") as f:
#     data = csv.reader(f)
#     for row in data:
#         if 'Jain' in row:
#             print(row)

# import csv
# f = open('D:\IDLE\.vscode\data.csv')
# csv_f = csv.reader()
# for row in csv_f:
#     print(row)

# with open(r"D:\IDLE\.vscode\test.txt",'r') as file1:
#     a = file1.read()
#     n = len(a)
#     while n>0:
#      for i in a:
#       if i==" ":
#          a.strip()
#       n-=1
#     file1.close()
# print(a)
# with open("come.txt",'w+') as file2:
#     file2.write(a)
#     print(file2.read())
#     print(file2.read())
#     file2.close()

# f1 = open(r"D:\IDLE\.vscode\test.txt","r+")
# f2 = open("come.txt","r+")
# l = f1.readlines()
# for line in l:
#     t = line.split()
#     for x in t:
#         f2.write(x)
#         f2.write(" ")
#     f2.write("\n")
# print(f1.read())

# file1 = open(r"D:\IDLE\.vscode\test.txt","r")
# file2 = open("Portal Express.txt","r")

# lst = file1.readlines()

# for i in lst :
#     word = i.split()
#     file2.write( " ".join(word)  )
#     file2.write("\n")

# print("Program has successfully run")
# print(file2.read())
# file2.close()
# file1.close()

# def read(file1,file2):
#     l = file1.readlines()
#     for line in l:
#         if line.split(" ~ ")[0] == "Atheletics":
#             file2.write(line)
#             file2.write("\n")
#     file1.close()
#     file2.close()
# file1 = open(r"D:\IDLE\.vscode\sports.dat","r")
# file2 = open("Atheletics.dat","w")
# read(file1,file2)



# f1 = open(r'D:\IDLE\.vscode\Info.txt',"r")
# for line in f1:   
#   x = line.split()
#   c = 12 - len(x[0])
#   print(x[0] + " "*c + "|" + "\t" + x[1])    
#   print()
          
# f1 = open(r"D:\IDLE\.vscode\Poem.txt","r")
# lines = f1.readlines()
# count_to = count_the = 0
# for i in str(lines).split():
#     if i=="the":
#         count_the+=1
#     if i=="to":
#         count_to+=1
# print("Total no. of (to) in file is: ",count_to)
# print("Total no. of (the) in file is: ",count_the)
# f1.close()

# def AMCount():
#     f1 = open(r"D:\IDLE\.vscode\Poem.txt","r")
#     count_a = count_m = 0
#     lines = f1.readlines()
#     for i in lines:
#         for j in i:
#             if j=="M" or j=="m":
#                 count_m+=1
#             if j=="A" or j=="a":
#                 count_a+=1
#     print("Total no. of M(s) or m(s) in file: ",count_m)
#     print("Total no. of A(s) or a(s) in file: ",count_a)  
# AMCount()

# f1 = open(r"D:\IDLE\.vscode\Poem.txt","r")
# a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# A = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# a_count = A_count = 0
# lines = f1.readlines()
# for i in lines:
#     for j in i:
#         for k in j:
#             if str(k) in a:
#                 a_count+=1
#             elif str(k) in A:
#                 A_count+=1
# print("Count of small letters: ",a_count)
# print("Count of big letters: ",A_count)        

# a = input("Enter the name of 1st file: ")
# b = input("Enter the name of 2nd file: ")
# f1 = open(a,'r')
# f2 = open(b,'w')
# A = f1.read()
# f2.write(A)
# f1.close()
# f2.close()

# a = input("Enter the name of 1st file: ")
# b = input("Enter the name of 2nd file: ")
# f1 = open(a,'r')
# f2 = open(b,'a')
# A = f1.read()
# f2.write(A)
# f1.close()
# f2.close()

# def DISPLAYWORDS():
#     f1 = open(r"D:\IDLE\.vscode\Poem.txt","r")
#     lines = f1.readlines()
#     for i in lines:
#       for j in i: 
#         if len(str(j)) < 4:
#               print(j,end=",")
# DISPLAYWORDS()

# f1 = open("UPPER.txt","w")
# f2 = open("LOWER.txt","w")
# f3 = open("OTHER.txt","w") 
# a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# A = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# count_a = count_A = count_O = 0
# b = True
# while b!="false":
#    b = input("enter the character or type false for exit: ")
#    if b in a:
#        count_a+=1
#    elif b in A:
#        count_A+=1
#    elif b=="false":
#        break
#    else:
#        count_O+=1
# print("total count of small letters: ",count_a)
# print("total count of BIG letters: ",count_A)
# print("total count of other letters: ",count_O)

# f1 = open(r"D:\IDLE\.vscode\LINES.txt","r")
# l = f1.readlines()
# count_1 = 0
# for i in l:
#     for j in i:
#         if j!="$":
#             count_1+=1
#         elif j=="$":
#             print(count_1)
#             break

# f1 = open("STRS.txt","w")
# while True:
#     a = input("ENTER THE TEXT YOU WANT or TYPE (END): ")
#     if a!="END":
#         f1.write(a)
#     elif a=="END":
#         break
# f1.close()

# import pickle
# file = open("member.dat","wb")
# dic = {}
# while True:
#     mem = int(input("Enter the Member_no.: "))
#     name = input("Enter the name: ")
#     dic["MemberNo."] = mem
#     dic["Name"] = name
#     pickle.dump(dic,file)
#     user = input("TYPE (END) to end the program \n type anything else to continue: ")
#     if user=="END":
#         break
# file.close()


# f1 = open(r"D:\IDLE\.vscode\NOTES.txt","r")
# while True:
#     a = f1.readline()
#     a = a.split()
#     if len(a)==5:
#         print(a)
    
# f1.close()
        




