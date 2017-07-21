__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/20/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3
from botocore.exceptions import ClientError


ec2 = boto3.client('ec2')

ALLOCATION_ID = 'eipalloc-e2dc438b'
try:
    response = ec2.release_address(AllocationId=ALLOCATION_ID)
    print('Address released')
except ClientError as e:
    print(e)

