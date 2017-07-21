__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/20/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3
import pprint


pp = pprint.PrettyPrinter()

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
# print(response)
pp.pprint(response)




