import mysql.connector as my
mycon = my.connect(host="localhost",username="root",passwd="123456",database="Shantanu2911")
cur = mycon.cursor()
cur.execute("insert into items")

