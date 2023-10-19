a, b, c=input("enter numbers: ").split()
a,b,c=int(a),int(b),int(c)
maxi=a
if maxi<b:
    maxi=b
if maxi<c:
    maxi=c
print("the largest no. is:",maxi)
