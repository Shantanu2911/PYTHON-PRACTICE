def pattern():
    for i in range(end):
        while b < end:
            if a[i]=="a":
                print(PRINT_A)
                b+=1
            elif a[0]=="b":
                PRINT_B
                b+=1
            elif a[0]=="c":
                PRINT_C
                b+=1
a=str(input("enter alphabet:"))
#print()
end=len(a)
b=0
def PRINT_A():
        str=""
        for row in range(7):
            for col in range(7):
                if(((col==1 or col==5)and row!=0)or((row==0 or row==3) and (col>1 and col<5))):
                    str=str+"⁕"
                else:
                    str=str+" "
            str=str+"\n"
        print(str)
def PRINT_B():
    if a[0]=="b":
        for row in range(7):
            for col in range(5):
                if(col==0)or(col==4 and (row!=0 and row!=3 and row!=6))or((row==0 or row==3 or row==6)and(col>0 and col<4)):
                    print("⁕",end="")
                else:
                    print(end=" ")
            print()
def PRINT_C():
    if a[0]=="c":
        for row in range(7):
            for col in range(5):
                if(row>=0 and col==0 and row!=0 and row!=6)or(col==1 and row==0)or(col==2 and row==0)or(col==3 and row==0)or(col==4 and row==0)or(col==1 and row==6)or(col==2 and row==6)or(col==3 and row==6)or(col==4 and row==6):
                    print("⁕ ",end="")
                else:
                    print(end=" ")
            print()

    

