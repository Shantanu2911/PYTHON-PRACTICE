
import math
A = input("Want to get the equation or get the roots \
                (e/r):")
print()

if A=="r" or A=="R" or A=="roots":
 print("IN YOUR QUADRATIC EQUATION Ax² + Bx + C :")
 a = float(input("ENTER THE VALUE OF A: "))
 b = float(input("ENTER THE VALUE OF B: "))
 c = float(input("ENTER THE VALUE OF C: "))

 if (b**2 - 4*a*c)<0:
     print()
     print("ROOTS ARE IMAGINARY")

 else:
     root_1 = (-b + ((b**2) + (-4*a*c))**0.5)/(2*a)
     root_2 = (-b - ((b**2) + (-4*a*c))**0.5)/(2*a)
     for i in range(1):
      if root_1 == math.ceil(root_1):
          root_1 = int(root_1)
      if root_2 == math.ceil(root_2):
         root_2 = int(root_2)
     print()
     print("THE ROOT OF THE QUADRATIC EQUATION ARE",root_1,"&",\
     root_2)

elif A=="e" or A=="E" or A=="equation":
    a = input("WANT TO ENTER THE ROOTS OR SUM AND PRODUCT OF IT\
           or \n WANT TO ENTER THE COEFFICIENTS (r/sp/c):")
    print()
    
    if a=="r" or a=="roots" or a=="R":
        A = float(input("ENTER THE VALUE OF 1st ROOT:"))
        B = float(input("ENTER THE VALUE OF 2nd ROOT:"))
        SUM = float(A + B)
        prd = float(A * B)
        for i in range(1):
         if SUM != 0 and SUM%int(SUM) == 0 :
            SUM = int(SUM)
        for i in range(1): 
         if prd != 0 and prd%int(prd) == 0:
            prd = int(prd)
            
        if SUM < 0 and prd < 0:
            print()
            print("THE EQUATION IS: x² +",str(-1*SUM)+"x",str(prd))
        elif SUM > 0 and prd > 0:
            print()
            print("THE EQUATION IS: x² -",str(SUM)+"x +",str(prd))
        elif SUM > 0 and prd <0:
            print()
            print("THE EQUATION IS: x² -",str(SUM)+"x",str(prd))
        elif SUM == 0 or prd == 0:
            if SUM==0 and prd==0:
                print("THE EQUATION IS: x²")
            elif SUM == 0:
                if prd<0:
                 print("THE EQUATION IS: x²"+str(prd))
                else:
                 print("THE EQUATION IS: x²+",str(prd))
            elif prd == 0:
                if SUM > 0:
                 print("THE EQUATION IS: x² -",str(SUM)+"x")
                elif SUM < 0:
                 print("THE EQUATION IS: x² +",str(-1*SUM)+"x")
        else:
            print()
            print("THE EQUATION IS: x² +",str(-1*SUM)+"x +",str(prd))

    elif a=="sp" or a=="SP":
        SUM= float(input("ENTER THE SUM:"))
        prd = float(input("ENTER THE PRODUCT:"))
        for i in range(1):
         if SUM != 0 and SUM%int(SUM) == 0:
            SUM = int(SUM)
        for i in range(1): 
         if prd != 0 and prd%int(prd) == 0:
            prd = int(prd)
            
        if SUM < 0 and prd < 0:
            print()
            print("THE EQUATION IS: x² +",str(-1*SUM)+"x",str(prd))
        elif SUM > 0 and prd > 0:
            print()
            print("THE EQUATION IS: x² -",str(SUM)+"x +",str(prd))
        elif SUM > 0 and prd <0:
            print()
            print("THE EQUATION IS: x² -",str(SUM)+"x",str(prd))
        elif SUM == 0 or prd == 0:
            if SUM==0 and prd==0:
                print("THE EQUATION IS: x²")
            elif SUM == 0:
                if prd<0:
                 print("THE EQUATION IS: x²"+str(prd))
                else:
                 print("THE EQUATION IS: x²+",str(prd))
            elif prd == 0:
                if SUM > 0:
                 print("THE EQUATION IS: x² -",str(SUM)+"x")
                elif SUM < 0:
                 print("THE EQUATION IS: x²+"+str(-1*SUM)+"x")
        else:
            print()
            print("THE EQUATION IS: x² +",str(-1*SUM)+"x +",str(prd))

    elif a=="c" or a=="C" or a=="coefficient":
        A = int(input("ENTER THE COEFFICIENT a:"))
        B = int(input("ENTER THE COEFFICIENT b:"))
        C = int(input("ENTER THE COEFFICIENT c:"))
        if A == 0:
          print("0 is the equation")
        else:
         SUM = float(-B/A)
         prd = float(C/A)
         for i in range(1):
          if SUM!=0 and SUM%int(SUM) == 0:
             SUM = int(SUM)
         for i in range(1): 
          if prd!=0 and prd%int(prd) == 0:
             prd = int(prd)
            
         if SUM < 0 and prd < 0:
             print()
             print("THE EQUATION IS: ","x² +",str(-1*SUM)+"x",str(prd))
         elif SUM > 0 and prd > 0:
             print
             print("THE EQUATION IS: ","x² -",str(SUM)+"x +",str(prd))
         elif SUM > 0 and prd <0:
             print()
             print("THE EQUATION IS: ","x² -",str(SUM)+"x",str(prd))
         elif SUM == 0 or prd == 0:
             if SUM==0 and prd==0:
                 print("THE EQUATION IS: x²")
             elif SUM == 0:
                 if prd<0:
                  print("THE EQUATION IS: x²"+str(prd))
                 else:
                  print("THE EQUATION IS: x²+",str(prd))
             elif prd == 0:
                 if SUM > 0:
                  print("THE EQUATION IS: x² -",str(SUM)+"x")
                 elif SUM < 0:
                  print("THE EQUATION IS: x²+",str(-1*SUM)+"x")
         else:
             print()
             print("THE EQUATION IS: ","x² +",str(-1*SUM)+"x +",str(prd))

    else:
        print("ERROR...")

else:
    print("ERROR...")
print("PROGRAM FINISHED !!!")
