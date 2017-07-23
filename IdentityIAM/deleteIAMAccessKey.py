

import boto3
import sys

userName = sys.argv[1]
accessKeyID = sys.argv[2]


print("aws Delete IAM Access Key")
print('user name : ', userName)
print('access key ID : ', accessKeyID)



# Create IAM client
iam = boto3.client('iam')

# Delete access key
iam.delete_access_key(
    AccessKeyId=accessKeyID,
    UserName=userName
)





