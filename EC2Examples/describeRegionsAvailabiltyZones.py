__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/20/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3

ec2 = boto3.client('ec2')

import pprint

pp = pprint.PrettyPrinter()



# Retrieves all regions/endpoints that work with EC2
response = ec2.describe_regions()
# print('Regions:', response['Regions'])
pp.pprint(response['Regions'])

# Retrieves availability zones only for region of the ec2 object
response = ec2.describe_availability_zones()
# print('Availability Zones:', response['AvailabilityZones'])
pp.pprint(response['AvailabilityZones'])

