#''' ARMSTRONG NUMBER '''


#a=int(input("ENTER A 3 DIGIT NUMBER"))
#a[0]=i
#a[1]=j
#a[2]=k
#if (i**2)+(j**2)+(k**2)==a:
#    print(a,"is a armstrong number")
#else:
#    print(a,"is not a armstrong number")


#a=int(input("ENTER A 3 DIGIT NUMBER"))
#print("a//2 is",a//10)
#print("a%2 is",a%10)
#print("a/2 is",a/2)
#print("a**2 is",a**2)



#summ=0                                            #a=407
#for a in range(100,999):
#    while(a>0):                                      #true        true        true        false
#        digit=a%10                                   #digit=7     digit=0     digit=4
#        summ+=digit**3                               #summ=343    summ=343    summ=407
#        a//=10                                       #a=40        a=4         a=0
#    if(a==summ):
#        print(num,"is an armstrong number")
#    else:
#        a+=1




for a in range(100,999):
    string=str(a)
    for ch in string:
        if float(a[0])**3 + float(a[1])**3+ float(a[2])**3 == a:
            print(a,"is an armstrong number")
        else:
            a+=1
