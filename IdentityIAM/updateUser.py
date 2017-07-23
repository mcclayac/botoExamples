



import boto3
import sys


originalName = sys.argv[1]
newName = sys.argv[2]

print('original name :', originalName)
print('new name :', newName)

# Create IAM client
iam = boto3.client('iam')

# Update a user name
iam.update_user(
    UserName=originalName,
    NewUserName=newName
)



