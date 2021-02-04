import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root@5",database="kludemo")
cu=mydb.cursor()
total=cu.execute("select * from Student")
print("Data in Student table is:")
for i in cu:
    print(i)
mydb.close()
