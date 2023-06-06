from pymongo import MongoClient
from .local_settings import username,password, aws_access_key, aws_secret_access_key, aws_storage_bucket, aws_default_acl
from datetime import datetime
from boto3 import client
import jwt

'''
AWS CONNECTION
'''

AWS_STORAGE_BUCKET_NAME = aws_storage_bucket
AWS_DEFAULT_ACL = aws_default_acl
AWS_BASE_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/"
def s3Client():
    return client('s3',aws_access_key_id=aws_access_key,aws_secret_access_key=aws_secret_access_key)

'''
DATABASE CONNECTION
'''

def clientOpen():
    # return MongoClient(f"mongodb://{username}:{password}@docdb-2021-08-31-04-49-08.cluster-cnx3ni4ekzmn.ap-south-1.docdb.amazonaws.com:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false")
    # return MongoClient(f"mongodb+srv://aiworld:i6TO1DZbtBzckOnx@mydb.xci1l.mongodb.net/mydb?retryWrites=true&w=majority") 
    return MongoClient(f"mongodb+srv://myworld:myworld@Cluster0.g3hr1.mongodb.net/liverooms?retryWrites=true&w=majority")


    