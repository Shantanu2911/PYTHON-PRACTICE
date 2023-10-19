a = [1,5,4,2,3]
n = len(a)
for i in range(n):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        else:
            i+=1

print(a)



a = [6,1,3,5,2,4]
n = len(a)
for i in range(1,n):
    key = a[i]
    j = i-1
    while j>=0 or key<a[j]:
        a[j+1] = a[j]
        j-=1
    else:
        a[j+1]=key

print(a)
    
    
