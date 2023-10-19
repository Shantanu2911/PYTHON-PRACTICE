x=int(input("ENTER A POSTIVE INTEGER: "))
s=0
for a in range(1,x):
    if x%a==0:
        s+=a
        a+=1
    else:
        a+=1
if s==x:
    print(x,"is a perfect no.")
else:
    print(x,"is not a perfect no.")
