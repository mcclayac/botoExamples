__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/23/17'
__revision__ = '$'
__revision_date__ = '$'





import boto3
import argparse
import textwrap

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
                                This program makes the
                                IAM User's Access key Active or Inactive
                                ----------------------
                                '''),
    epilog='''
        BigManSoftware Copyright 2017 - BigmanSoftware
        Developed by : Tony McClay
        Date: 7/24/2017 
        All Rights reserved''')

parser.add_argument("iamUser", help="The IAM User to delete the key from")
parser.add_argument("accessKey", help="This is the IAM Access key to be deleted")
parser.add_argument("status", help="This is the status set", choices=['Active','Inactive'], default='Active')
args = parser.parse_args()

print(args)
programName = parser.prog
iamUser = args.iamUser
accessKey = args.accessKey
status = args.status


print(programName)
print("iam User : " + iamUser)
print("Access Key : " + accessKey)
print("Status : " + status)

# Create IAM client
iam = boto3.client('iam')

# # Update access key to be active
iam.update_access_key(
    AccessKeyId=accessKey,
    Status=status,
    UserName=iamUser
)
print("--------------------------")
print("Access Key : " + accessKey)
print("Status Set to : " + status)
print("--------------------------")




