import mysql.connector as my
con = my.connect(host='127.0.0.1',username='root',password='123456',database='Shantanu2911')
cur = con.cursor()
f1 = cur.execute("select * from stu1")
for i in range(10):
 print(cur.fetchmany())
