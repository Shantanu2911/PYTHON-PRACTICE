def A():
    str=""
    for row in range(7):
        for col in range(7):
            if(((col==1 or col==5)and row!=0)or((row==0 or row==3) and (col>1 and col<5))):
                str=str+"⁕"
            else:
                str=str+" "
        str=str+"\n"
    print(str)
def B():
    for row in range(7):
        for col in range(5):
            if(col==0)or(col==4 and (row!=0 and row!=3 and row!=6))or((row==0 or row==3 or row==6)and(col>0 and col<4)):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
def C():
    for row in range(7):
        for col in range(5):
            if(row>=0 and col==0 and row!=0 and row!=6)or(col==1 and row==0)or(col==2 and row==0)or(col==3 and row==0)or(col==4 and row==0)or(col==1 and row==6)or(col==2 and row==6)or(col==3 and row==6)or(col==4 and row==6):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
def D():
    for row in range(7):
        for col in range(5):
            if(row>=0 and col==0)or(row==0 and col>0 and col<3)or(col==4 and row>0 and row<6)or(row==6 and col>0 and col<3):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
def E():
    for row in range(7):
        for col in range(5):
            if(row>=0 and col==0)or(row==0 and col>=0)or(row==6 and col>=0)or(row==3 and col<=2):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
def F():
    for row in range(7):
        for col in range(5):
            if(row>=0 and col==0)or(row==0 and col>=0)or(row==3 and col<=2):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
def G():
    for row in range(5):
        for col in range(6):
            if(row==0 and col>=1 and col!=5)or(col==0 and row>=1 and row!=4)or(row==4 and col<=2 and col!=0)or(col==3 and row>=2 and row!=4)or(col==4 and row>=2):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
def H():
   for row in range(7):
        for col in range(5):
            if col==0 or col==4 or(row==3 and (col>0 and col<4)):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
def I():
    for row in range(5):
        for col in range(5):
            if(row==0 and col>=0)or(row==4 and col>=0)or(col==4 and row>=0):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
def J():
    for row in range(5):
        for col in range(5):
            if(row==0 and col>=0)or(row==4 and col<2)or(col==4 and row>=0 and row!=4):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
def K():
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=0)or(row==0 and col==3)or(row==1 and col==2)or(row==2 and col==1)or(row==3 and col==2)or(row==4 and col==3):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
def L():
    for row in range(5):
        for col in range(5):
            if(row>=0 and col==0)or(row==4 and col>=1):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
def M():
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=0)or(col==4 and row>=0)or(row==1 and col==1)or(row==2 and col==2)or(row==1 and col==3):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
def N():
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=0)or(col==4 and row>=0)or(row==1 and col==1)or(row==2 and col==2)or(row==3 and col==3):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
def O():
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=0)or(col==4 and row>=0)or(row==4 and col>=0)or(row==0 and col>=0):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
def P():
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=0)or(col<=3 and row==0)or(row<=2 and col==3)or(row==2 and col<=3):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
def Q():
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=1 and row!=4)or(row==0 and col>=1 and col!=4 and col!=3)or(col==4 and row>=1 and row!=3)or(row==4 and col>=1 and col!=3)or(col==3 and row==3)or():
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
def R():
    for row in range(6):
        for col in range(4):
            if(col==0 and row>=0)or(col==1 and row==0)or(col==1 and row==3)or(col==2 and row==0)or(col==2 and row==2)or(col==2 and row==4)or(col==3 and row==1)or(col==3 and row==5):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
def S():
    str=""
    for row in range(0,7):
        for col in range(0,7):
            if(((row==0 or row==3 or row==6)and col>1 and col<5)or(col==1 and(row==1 or row==2 or row==6))or(col==5 and (row==0 or row==4 or row==5))):
                str=str+"⁕"
            else:
                  str=str+" "
        str=str+"\n"
    print(str)
def T():
    for row in range(5):
        for col in range(5):
            if(row==0 and col>=0)or(col==4 and row>=1):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
def U():
    for row in range(5):
        for col in range(5):
            if(col==0 and row>=0 and row!=4)or(col==4 and row>=0 and row!=4):
                print("⁕",end="")
            elif(row==4 and col>=0):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
def V():
    for row in range(5):
        for col in range(5):
            if(col==0 and row<=2)or(col==4 and row<=2)or(row==3 and col==1)or(row==3 and col==3)or(col==2 and row==4):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
def W():
    for row in range(5):
        for col in range(5):
            if(col==0 and row<=3)or(col==4 and row<=3)or(col==1 and row==4)or(col==3 and row==4)or(col==2 and row==3):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
def X():
    for row in range(5):
        for col in range(5):
            if(col==0 and row==0)or(col==1 and row==1)or(col==2 and row==2)or(col==3 and row==3)or(col==4 and row==4)or(row==0 and col==4)or(row==1 and col==3)or(row==3 and col==1)or(row==4 and col==0):
                print("⁕",end="")
            else:
                print(end=" ")
        print()
def Y():
    for row in range(5):
        for col in range(5):
            if(col==0 and row==0)or(col==1 and row==1)or(col==2 and row==2)or(row==0 and col==4)or(row==1 and col==3)or(row==3 and col==1)or(row==4 and col==0):
                print("⁕ ",end="")
            else:
                print(end=" ")
        print()
def Z():
    for row in range(6):
        for col in range(5):
            if(row==0 and col>=0)or(row==5 and col>=0)or(col==4 and row==1)or(col==3 and row==2)or(col==2 and row==3)or(col==1 and row==4):
                print("⁕",end="")
            else:
                print(end=" ")
        print()

string=input("Enter your name:-")
l=len(string)
s2=" "
for i in range(0,l):
    if string[i]=="A"or string[i]=="a":
        A()
        i+=1
    elif string[i]=="B" or string[i]=="b":
        B()
        i+=1
        print()
    elif string[i]=="C" or string[i]== "c":
        C()
        i+=1
        print()
    elif string[i]=="d" or string[i]=="D":
        D()
        i+=1
        print()
    elif string[i]=="E" or string[i]=="e":
        E()
        i+=1
        print()
    elif string[i]=="F" or string[i]=="f":
        F()
        i+=1
        print()
    elif string[i]=="G" or string[i]=="g":
        G()
        i+=1
        print()
    elif string[i]=="H" or string[i]=="h":
        H()
        i+=1
        print()
    elif string[i]=="I" or string[i]=="i":
        I()
        i+=1
        print()
    elif string[i]=="J" or string[i]=="j":
        J()
        i+=1
        print()
    elif string[i]=="K" or string[i]=="k":
        K()
        i+=1
        print()
    elif string[i]=="L" or string[i]=="l":
        L()
        i+=1
        print()
    elif string[i]=="M" or string[i]=="m":
        M()
        i+=1
        print()
    elif string[i]=="N" or string[i]=="n":
        N()
        i+=1
        print()
    elif string[i]=="O" or string[i]=="o":
        O()
        i+=1
        print()
    elif string[i]=="P" or string[i]=="p":
        P()
        i+=1
        print()
    elif (string[i]=="Q" or string[i]=="q"):
        Q()
        i+=1
        print()
    elif (string[i]=="R" or string[i]=="r"):
        R()
        i+=1
        print()
    elif (string[i]=="S" or string[i]=="s"):
        S()
        i+=1
    elif (string[i]=="T" or string[i]=="t"):
        T()
        i+=1
        print()
    elif (string[i]=="U" or string[i]=="u"):
        U()
        i+=1
        print()
    elif (string[i]=="V" or string[i]=="v"):
        V()
        i+=1
        print()
    elif (string[i]=="W" or string[i]=="w"):
        W()
        i+=1
        print()
    elif (string[i]=="X" or string[i]=="x"):
        X()
        i+=1
        print()
    elif (string[i]=="Y" or string[i]=="y"):
        Y()
        i+=1
        print()
    elif (string[i]=="Z" or string[i]=="z"):
        Z()
        i+=1
        print()
