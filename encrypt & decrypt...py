x = input("enter the message: ")
x = list(x)
l = len(x)
a = input("do wanna encrypt(e) or decrypt(d): ")
key = int(input("enter the key (key of encryption...) : "))

if key >= l/2:
     print("key should be small...")
        
elif a == "encrypt" or a == "e":
    countt = 0
    for i in range(0,l):
        if i%key == 0 and i<(l-key):
            x[i],x[i+key] = x[i+key],x[i]
            countt += 1
    x = "".join(x)
    print(x)
    print("count =",countt)
    
elif a == "decrypt" or a == "d":
    count = int(input("enter count: "))
    for j in range(count):
        for i in range(0,l):
             if i%key == 0 and (i<l-key):
                  x[i],x[i+key] = x[i+key],x[i]
    x = "".join(x)
    print(x)

else:
    print("something's wrong...")
