import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root@5",database="kludemo")
cu=mydb.cursor()
def all_opr():
    while(True):
        print("1.Insert Record\n2.Update Record\n3.Delete Record\n4.Exit")
        n = int(input("Enter your Choice:"))
        if n==1:
            id = int(input("Enter your ID: "))
            name = input("Enter your Name: ")
            insertv = "insert into Student values(%s,%s)"
            value = (id, name)
            cu.execute(insertv, value)
            print(cu.rowcount, "rows affected")
            mydb.commit();
        elif n==2:
            id = int(input("Enter your ID: "))
            name = input("Enter your Name: ")
            updatev = "update Student set name=%s where id=%s"
            value = (name,id)
            cu.execute(updatev, value)
            print(cu.rowcount, "rows affected")
            mydb.commit();
        elif n==3:
            id = int(input("Enter your ID: "))
            deletev="delete from Student where id=%d"
            value=id
            cu.execute(deletev,value)
            print(cu.rowcount, "rows affected")
            mydb.commit();
        elif n==4:
            mydb.close()


all_opr()



