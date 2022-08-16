import pymysql
mydb=pymysql.connect('ivnc-test-rds.cprqglsudqxv.us-east-1.rds.amazonaws.com', 'ivnctestadmin', 'testadmin!202022')
mycursor=mydb.cursor() #cursor object provides connection between sql database and sql queries
if(mydb):
    print("connection successful")
else:
    print("connection unsuccessful")
mycursor.execute("show databases")
for i in mycursor:
    print(i)
