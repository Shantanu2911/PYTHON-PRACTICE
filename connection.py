import mysql.connector
con = mymysql.connector.connect(host='localhost',user = 'root',\
                                password = 'tiger',database = 'classxii')
cur = con.cursor()

t = input("Enter Stream: ")
cur.execute("Select * from student e=where stream='%s'"%t)
data = cur.fetchall()
for i in data:
    print(i)
print("Total records retrieved:",cur.rowcount)
