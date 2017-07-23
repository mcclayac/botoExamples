

import boto3
import sys


userName = sys.argv[1]

print("aws Delete User")
print('user name :', userName)


# Create IAM client
iam = boto3.client('iam')

# Delete a user
iam.delete_user(
    UserName=userName
)


