__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/20/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3
from botocore.exceptions import ClientError
import pprint
pp = pprint.PrettyPrinter()


ec2 = boto3.client('ec2')

SECURITY_GROUP_ID = ['sg-b27c75db','sg-b04a8ed9','sg-750f061c']

try:
    response = ec2.describe_security_groups(GroupIds=SECURITY_GROUP_ID)
    pp.pprint(response)
except ClientError as e:
    print(e)


