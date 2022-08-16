import boto3
import os
os.system("aws s3 ls")
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
