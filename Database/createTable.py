import mysql.connector

myCon = mysql.connector.connect(host="localhost", user="root", password="Tanav23o8",auth_plugin='mysql_native_password', database='ekaja_db')

print(myCon)

mycursor = myCon.cursor()


try:
    mycursor.execute("create table emp(eno int(6), ename varchar(30), sal int(6));")
    print("table is created")

except:
    myCon.rollback()

myCon.close()