import boto3
import os
import datetime
import time
from datetime import datetime, timedelta
 
def lambda_handler(event, context):
    
    bucket_name = 'infor-devops-dev-appdata-us-east-1'
    #Anyone can set this prefix to versions2 which is our test folder to test.
    prefix = 'mongoose/patches/framework/versions/'
    keep_for_days = 180
    s3 = boto3.resource('s3', region_name ='us-east-1')
    bucket =  s3.Bucket(bucket_name)
    s3objects = bucket.objects.filter(Prefix=prefix)
    #What this loop is doing is effectively deleting anything within the versions folder that is set to be older than six months old.
    for objects in s3objects:
        print('s3 key: ' + objects.key)
        print(objects.last_modified.strftime('%m/%d/%Y %H:%M:%S'))

        date_diff = abs(datetime.today() - objects.last_modified.replace(tzinfo=None)).days
        print('obj date_diff: ' + str(date_diff))
        
        if objects.key == prefix:
            print('Keeping main prefix', prefix)
            print('--')
            continue
        if date_diff >= keep_for_days:   
            print('DELETING ' + bucket_name + ' ' + objects.key)
            print (keep_for_days)
            ##WARNING## Please comment this line out for testing/debugging purposes!!
            print(s3.Object(bucket.name, key=objects.key).delete())
        else:
            print('Retained Newer Objects')

        print('--')
#If you want to test please uncomment these lines.     
#event = ''
#context = ''
#lambda_handler (event, context)