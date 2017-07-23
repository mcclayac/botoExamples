__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/23/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3
import sys


userName = sys.argv[1]


print("aws List User Access Keys")
print("user name :" + userName)


# Create IAM client
iam = boto3.client('iam')

# List access keys through the pagination interface.
paginator = iam.get_paginator('list_access_keys')
for response in paginator.paginate(UserName=userName):
    for accessID in response['AccessKeyMetadata']:
        print('Access ID : ' + accessID['AccessKeyId'] + '\tStatus :' + accessID['Status'])

# for accessID in paginator.paginate(UserName=userName)['AccessKeyMetadata']:
#     print('Access ID : ' + accessID['AccessKeyId'] + '\tStatus :' + accessID['Status'])