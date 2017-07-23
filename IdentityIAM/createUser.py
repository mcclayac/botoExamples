

import boto3
import sys


IAM_USER_NAME = sys.argv[1].lower()

# Create IAM client
iam = boto3.client('iam')

# Create user
response = iam.create_user(
    UserName=IAM_USER_NAME
)

# print(response)
userName = response['User']['UserName']
arn = response['User']['Arn']
print('User Name :', userName, ' arn :', arn)




