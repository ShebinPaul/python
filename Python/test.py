import mysql.connector
mydb=mysql.connector.connect(host="ivncdwdevdb1.cprqglsudqxv.us-east-1.rds.amazonaws.com",user="ivncdwadm",passwd="ivncdwadmin&2022")
mycursor=mydb.cursor() #cursor object provides connection between sql database and sql queries
if(mydb):
    print("connection successful")
else:
    print("connection unsuccessful")
mycursor.execute("show databases")
for i in mycursor:
    print(i)
