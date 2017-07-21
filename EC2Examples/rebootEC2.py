__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/20/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3
from botocore.exceptions import ClientError


ec2 = boto3.client('ec2')

instance_id = 'i-04d63dc650b4652ff'

try:
    ec2.reboot_instances(InstanceIds=[instance_id], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You don't have permission to reboot instances.")
        raise

try:
    response = ec2.reboot_instances(InstanceIds=[instance_id], DryRun=False)
    print('Success', response)
except ClientError as e:
    print('Error', e)