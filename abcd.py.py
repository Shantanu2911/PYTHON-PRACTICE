
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

string=input("enter a string")
l=len(string)
s2=""
for i in range(0,l):
    if (string[i]=="A" or "a"):
        print(A())
        i+=1
    elif (string[i]=="B" or "b"):
        print(B())
        i+=1
    elif (string[i]=="C" or "c"):
        print(C())
        i+=1
    elif (string[i]=="d" or "D"):
        print(D())
        i+=1
    elif (string[i]=="E" or "e"):
        print(E())
        i+=1
    elif (string[i]=="F" or "f"):
        print(F())
        i+=1
    elif (string[i]=="G" or "g"):
        print(G())
        i+=1
    elif (string[i]=="H" or "h"):
        print(H())
        i+=1
    elif (string[i]=="I" or "i"):
        print(I())
        i+=1
    elif (string[i]=="J" or "j"):
        print(J())
        i+=1
    elif (string[i]=="K" or "k"):
        print(K())
        i+=1
    elif (string[i]=="L" or "l"):
        print(L())
        i+=1
    elif (string[i]=="M" or "m"):
        print(M())
        i+=1
    elif (string[i]=="N" or "n"):
        print(N())
        i+=1
    elif (string[i]=="O" or "o"):
        print(O())
        i+=1
    elif (string[i]=="P" or "p"):
        print(P())
        i+=1
    elif (string[i]=="Q" or "q"):
        print(Q())
        i+=1
    elif (string[i]=="R" or "r"):
        print(R())
        i+=1
    elif (string[i]=="S" or "s"):
        print(S())
        i+=1
    elif (string[i]=="T" or "t"):
        print(T())
        i+=1
    elif (string[i]=="U" or "u"):
        print(U())
        i+=1
    elif (string[i]=="V" or "v"):
        print(V())
        i+=1
    elif (string[i]=="W" or "w"):
        print(W())
        i+=1
    elif (string[i]=="X" or "x"):
        print(X())
        i+=1
    elif (string[i]=="Y" or "y"):
        print(Y())
        i+=1
    elif (string[i]=="Z" or "z"):
        print(Z())
        i+=1
