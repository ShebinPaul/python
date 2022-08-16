import mysql.connector
mydb=mysql.connector.connect(host="ivnc-test-rds.cprqglsudqxv.us-east-1.rds.amazonaws.com",user="ivnctestadmin",passwd="testadmin!202022")
mycursor=mydb.cursor() #cursor object provides connection between sql database and sql queries
if(mydb):
    print("connection successful")
else:
    print("connection unsuccessful")
mycursor.execute("show databases")
for i in mycursor:
    print(i)
