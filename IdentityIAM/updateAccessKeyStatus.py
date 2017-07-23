__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/23/17'
__revision__ = '$'
__revision_date__ = '$'





import boto3
import sys


applicationName = sys.argv[0]

if len(sys.argv) != 3 :
    print("Must be 3 arguments")
    print(applicationName + " user_name access_key_id status(active|deactive)")
    sys.exit(0)

iamUserName = sys.argv[1]
accessKeyID = sys.argv[2]
status = sys.argv[3]


# Create IAM client
iam = boto3.client('iam')

# Update access key to be active
iam.update_access_key(
    AccessKeyId='ACCESS_KEY_ID',
    Status='Active',
    UserName='IAM_USER_NAME'
)



