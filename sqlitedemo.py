import sqlite3
db=sqlite3.connect("klu.db");
cur=db.cursor();
cur.execute("create table student1(id int(3),name text(20))");
db.commit();
db.close();
print("Table is created");