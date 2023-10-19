myfile = open(r"D:\Study\OTHER\test1.txt","r+")
str1 = " "
size = 0
tsize = 0
while str1:
 str1 = myfile.readline()
 tsize += len(str1)
 size += len(str1.strip())
print("size of file after removing EOL characters:",size)
print("original size:",tsize)
myfile.close()