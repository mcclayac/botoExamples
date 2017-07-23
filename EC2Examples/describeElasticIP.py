__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/20/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3
import sys


# //  instance_id = sys.argv[2]
region_name = sys.argv[1].lower()

print('region name :', region_name)

ec2 = boto3.client('ec2', region_name=region_name)
filters = [
    {'Name': 'domain', 'Values': ['vpc']}
]
response = ec2.describe_addresses(Filters=filters)
# print(response)

for allocid in response['Addresses']:
    print('Allocationd id :', allocid['AllocationId'], ' Public ip :', allocid['PublicIp'])


