__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/20/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3

KEY_PAIR_NAME = 'botoOhioKeyPair'

ec2 = boto3.client('ec2')
response = ec2.delete_key_pair(KeyName=KEY_PAIR_NAME)
print(response)