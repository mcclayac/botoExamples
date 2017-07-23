

import boto3
import sys


print("aws Create Access Keys")

userName = sys.argv[1]
print("user name :", userName)




# Create IAM client
iam = boto3.client('iam')

# Create an access key
response = iam.create_access_key(
    UserName=userName
)

fileName = response['AccessKey']['UserName']
fileName = userName + '.txt'


print('Writing FileName')
print('file name :', fileName)

userName = response['AccessKey']['UserName']
accessKeyID = response['AccessKey']['AccessKeyId']
secretAccessKey = response['AccessKey']['SecretAccessKey']


file = open(fileName, "w")
str = "user name : " + userName + "\n"
file.write(str)
print(str)

str = "Access key ID : " + accessKeyID + "\n"
file.write(str)
print(str)

str = "Secret Access Key : " + secretAccessKey + "\n"
file.write(str)
print(str)

file.close()







