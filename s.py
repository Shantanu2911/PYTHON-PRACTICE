a=str(input("enter alphabet:"))
print()
if a[0]=="a":
    str=""
    for row in range(7):
        for col in range(7):
            if(((col==1 or col==5)and row!=0)or((row==0 or row==3) and (col>1 and col<5))):
                str=str+"⁕"
            else:
                str=str+" "
        str=str+"\n"
    print(str)
if a[0]=="b":
    for row in range(7):
        for col in range(5):
            if(col==0)or(col==4 and (row!=0 and row!=3 and row!=6))or((row==0 or row==3 or row==6)and(col>0 and col<4)):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
if a[0]=="c":
    for row in range(7):
        for col in range(5):
            if(row>=0 and col==0 and row!=0 and row!=6)or(col==1 and row==0)or(col==2 and row==0)or(col==3 and row==0)or(col==4 and row==0)or(col==1 and row==6)or(col==2 and row==6)or(col==3 and row==6)or(col==4 and row==6):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
if a[0]=="d":
    for row in range(7):
        for col in range(5):
            if(row>=0 and col==0)or(row==0 and col>0 and col<3)or(col==4 and row>0 and row<6)or(row==6 and col>0 and col<3):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
if a[0]=="e":
    for row in range(7):
        for col in range(5):
            if(row>=0 and col==0)or(row==0 and col>=0)or(row==6 and col>=0)or(row==3 and col<=2):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
if a[0]=="f":
    for row in range(7):
        for col in range(5):
            if(row>=0 and col==0)or(row==0 and col>=0)or(row==3 and col<=2):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
if a[0]=="g":
    for row in range(5):
        for col in range(6):
            if(row==0 and col>=1 and col!=5)or(col==0 and row>=1 and row!=4)or(row==4 and col<=2 and col!=0)or(col==3 and row>=2 and row!=4)or(col==4 and row>=2):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
if a[0]=="h":
    for row in range(7):
        for col in range(5):
            if col==0 or col==4 or(row==3 and (col>0 and col<4)):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
if a[0]=="i":
    for row in range(5):
        for col in range(5):
            if(row==0 and col>=0)or(row==4 and col>=0)or(col==4 and row>=0):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
if a[0]=="j":
    for row in range(5):
        for col in range(5):
            if(row==0 and col>=0)or(row==4 and col<2)or(col==4 and row>=0 and row!=4):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
if a[0]=="k":
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=0)or(row==0 and col==3)or(row==1 and col==2)or(row==2 and col==1)or(row==3 and col==2)or(row==4 and col==3):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
if a[0]=="l":
    for row in range(5):
        for col in range(5):
            if(row>=0 and col==0)or(row==4 and col>=1):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
if a[0]=="m":
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=0)or(col==4 and row>=0)or(row==1 and col==1)or(row==2 and col==2)or(row==1 and col==3):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
if a[0]=="n":
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=0)or(col==4 and row>=0)or(row==1 and col==1)or(row==2 and col==2)or(row==3 and col==3):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
if a[0]=="o":
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=0)or(col==4 and row>=0)or(row==4 and col>=0)or(row==0 and col>=0):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
if a[0]=="p":
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=0)or(col<=3 and row==0)or(row<=2 and col==3)or(row==2 and col<=3):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
if a[0]=="q":
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=1 and row!=4)or(row==0 and col>=1 and col!=4 and col!=3)or(col==4 and row>=1 and row!=3)or(row==4 and col>=1 and col!=3)or(col==3 and row==3)or():
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
if a[0]=="r":
    for row in range(6):
        for col in range(4):
            if(col==0 and row>=0)or(col==1 and row==0)or(col==1 and row==3)or(col==2 and row==0)or(col==2 and row==2)or(col==2 and row==4)or(col==3 and row==1)or(col==3 and row==5):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
if a[0]=="s":
    str=""
    for row in range(0,7):
        for col in range(0,7):
            if(((row==0 or row==3 or row==6)and col>1 and col<5)or(col==1 and(row==1 or row==2 or row==6))or(col==5 and (row==0 or row==4 or row==5))):
                str=str+"⁕"
            else:
                  str=str+" "
        str=str+"\n"
    print(str)
if a[0]=="t":
    for row in range(5):
        for col in range(5):
            if(row==0 and col>=0)or(col==4 and row>=1):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
if a[0]=="u":
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=0 and row!=4)or(col==4 and row>=0 and row!=4):
                print("⁕",end="")
            elif(row==4 and col>=0):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
if a[0]=="v":
    for row in range(5):
        for col in range(5):
            if(col==0 and row<=2)or(col==4 and row<=2)or(row==3 and col==1)or(row==3 and col==3)or(col==2 and row==4):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
if a[0]=="w":
    for row in range(5):
        for col in range(5):
            if(col==0 and row<=3)or(col==4 and row<=3)or(col==1 and row==4)or(col==3 and row==4)or(col==2 and row==3):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
if a[0]=="x":
    for row in range(5):
        for col in range(5):
            if(col==0 and row==0)or(col==1 and row==1)or(col==2 and row==2)or(col==3 and row==3)or(col==4 and row==4)or(row==0 and col==4)or(row==1 and col==3)or(row==3 and col==1)or(row==4 and col==0):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
if a[0]=="y":
    for row in range(5):
        for col in range(5):
            if(col==0 and row==0)or(col==1 and row==1)or(col==2 and row==2)or(row==0 and col==4)or(row==1 and col==3)or(row==3 and col==1)or(row==4 and col==0):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
if a[0]=="z":
    for row in range(6):
        for col in range(5):
            if(row==0 and col>=0)or(row==5 and col>=0)or(col==4 and row==1)or(col==3 and row==2)or(col==2 and row==3)or(col==1 and row==4):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
#    0 1 2 3 4
#0   * * * * *     
#1           *
#2         *       
#3       *
#4     * 
#5   * * * * *
else:
    print('\n')

    
