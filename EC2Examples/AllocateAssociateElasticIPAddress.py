__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/20/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

INSTANCE_ID = 'i-0764e4f8c34367106'

try:
    allocation = ec2.allocate_address(Domain='vpc')
    response = ec2.associate_address(AllocationId=allocation['AllocationId'],
                                     InstanceId=INSTANCE_ID)
    print(response)
except ClientError as e:
    print(e)

