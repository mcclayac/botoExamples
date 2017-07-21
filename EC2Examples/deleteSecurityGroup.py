__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/20/17'
__revision__ = '$'
__revision_date__ = '$'



import boto3
from botocore.exceptions import ClientError

# Create EC2 client
ec2 = boto3.client('ec2')

SECURITY_GROUP_ID = 'sg-a7b85dcf'
# Delete security group
try:
    response = ec2.delete_security_group(GroupId=SECURITY_GROUP_ID)
    print('Security Group Deleted')
except ClientError as e:
    print(e)


