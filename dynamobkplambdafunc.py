import boto3
import time
from botocore.exceptions import ClientError
import json
import os
aws_region = os.getenv('AWS_DEFAULT_REGION')
dynamoTable = os.getenv('DynamoTestTable')
dynamoDBBackupName = 'Dynamo_Backup'
ddb = boto3.client('dynamodb', region_name=aws_region)
def lambda_handler (event, context):
    
        print('Backup started')
        ddb.create_backup(TableName=dynamoTable,BackupName=dynamoDBBackupName)
        print('Backup created')