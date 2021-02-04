import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root@5",database="kludemo")
cu=mydb.cursor()
cu.execute("delete from Student where id=30669");
mydb.commit();
mydb.close()