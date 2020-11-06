#while doing connection faced issues connecting to DB
#then uninstlled-> pip3 uninstall mysql-connector-python
#installed back-> pip3 install mysql-connector-python

import mysql.connector
#create the connection object
myCon = mysql.connector.connect(host="localhost", database='abc', user="root", password="Tanav23o8",
                                auth_plugin='mysql_native_password')
print(myCon)

#create the cursor object
mycursor = myCon.cursor()

print(mycursor)
myCon.close()


