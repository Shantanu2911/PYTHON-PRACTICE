# Python code to demonstrate naive method
# to compute factorial
#n = int(input("ENTER A NUMBER"))
#fact = 1
#  
#for i in range(1,n+1):
#    fact = fact * i
#      
#print ("The factorial of",n,"is : ",end="")
#print (fact)

#   ''' x+x**2/2!-x**3/3!+...-x**n/n!

x=int(input("ENTER THE VALUE OF X"))     #x=2
n=int(input("ENTER THE VALUE OF N"))     #n=3
s=x                                      #s=2
sign=+1               
for a in range(2,n+1):                   #2          
    f=1                                  #f=1        
    for i in range(1,a+1):               #1
        f*=i                             #f=1
    term=((x**a)*sign)/f                 #term=1
    s+=term                              #s=3
    sign*=-1                             #sign=-1
print("sum of first",n,"terms :",s)        
