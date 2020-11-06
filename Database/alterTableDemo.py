import mysql.connector

myCon = mysql.connector.connect(host="localhost", user="root", password="Tanav23o8",auth_plugin='mysql_native_password', database='ekaja_db')

print(myCon)

mycursor = myCon.cursor()


try:
    #mycursor.execute("alter table emp add mobile_no int(10)")
    #mycursor.execute("alter table emp add location varchar(30)")
    #mycursor.execute("alter table emp modify location varchar(35)")
    mycursor.execute("alter table emp drop location")
    print("table is alterated")

except:
    myCon.rollback()

myCon.close()