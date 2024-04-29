print("Hello world from github repo........")

import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="bharats",
                               passwd="cybage@123",
                               database="acme")

if mydb.is_connected == False:
    print("Unable to connect to db")

mycursor = mydb.cursor()
command = "select * from student"
#command = "UPDATE student set college = 'vjit123' where name = 'Bharat'"

try:
    mycursor.execute(command)
    #mydb.commit()
    #print(mycursor.rowcount, "rows updated...")
except:
    pass
    #mydb.rollback()
finally:
    pass

results = mycursor.fetchall()

for i in results:
    print(i)

