# 1+x+x**2+x**3+...x**n
x=float(input("ENTER THE VALUE OF X: "))
n=int(input("ENTER THE VALUE OF N: "))
y=0
for i in range(0,n+1):
    y+=x**i
print(y,"is the value of the series")
