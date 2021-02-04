import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root@5",database="kludemo")
cu=mydb.cursor()
id = int(input("Enter your ID: "))
deletev="delete from Student where id=%d"
value=(id)
cu.execute(deletev,value)
mydb.commit();
mydb.close()