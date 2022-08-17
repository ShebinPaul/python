# RDS Connection
# --------------
import mysql.connector
import sys
import boto3
import os
import pandas
 
ENDPOINT="ivncdwdevdb1.cprqglsudqxv.us-east-1.rds.amazonaws.com"
PORT="3306"
USER="ivncdwccfdev1"
REGION="us-east-1"
DBNAME="ccf_edp_audit_information"
PWORD="Developer@123dev"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'
 
# Get credentials from .aws/credentials
#session = boto3.Session(profile_name='default')
client = session.client('rds')
 
token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)
 
try:
    # conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=token, port=PORT, database=DBNAME, ssl_ca='SSLCERTIFICATE')
    conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=PWORD, port=PORT, database=DBNAME)
    print('Connected to RDS DB')
    qrDF = pandas.read_sql('select * from ctl_dataset_master limit 2', conn)
    # cur = conn.cursor()
    # qr = conn.execute('select * from ctl_dataset_master limit 2')
    # qrDF = pandas.DataFrame(qr.fetchall())
    # qrDF.columns = qr.keys()
    print(qrDF)
except Exception as e:
    print("Database connection failed due to {}".format(e))
