



import boto3

# Create IAM client
iam = boto3.client('iam')

# List users with the pagination interface
paginator = iam.get_paginator('list_users')
# for response in paginator.paginate():
#     print(response)
for response in paginator.paginate():
    for user in response['Users']:
        # print(user)
        print(user['UserName'], '\t\t', user['Arn'])


