#1.import mysql connection
import mysql.connector

#2.create the connection object
myCon = mysql.connector.connect(host="localhost", user="root", password="Tanav23o8",auth_plugin='mysql_native_password', database="ekaja_DB")

print(myCon)

#3.create the cursor object
mycursor = myCon.cursor()
print(mycursor)
#4.execute the query(always write/execute queries in exception handling
try:
    mycursor.execute("create database ekaja_DB;")
    print("database is created")
    dblist = mycursor.execute("show databases;")
except:
    myCon.rollback()

for d in mycursor:
    print(d)

#5.close the connection
myCon.close()

