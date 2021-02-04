import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root@5",database="kludemo")
cu=mydb.cursor()
print("Enter your ID: ")
id=int(input())
print("Enter your Name: ")
name=input()
insertv="insert into Student values(%s,%s)"
value=(id,name)
cu.execute(insertv,value)
print(cu.rowcount,"rows affected")
mydb.commit();
mydb.close()