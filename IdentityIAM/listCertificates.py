__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/24/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3

# Create IAM client
iam = boto3.client('iam')

# List server certificates through the pagination interface
paginator = iam.get_paginator('list_server_certificates')
for response in paginator.paginate():
    print(response['ServerCertificateMetadataList'])


