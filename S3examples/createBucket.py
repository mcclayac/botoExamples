__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/27/17'
__revision__ = '$'
__revision_date__ = '$'



import boto3
import argparse
import textwrap

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
                                This program Creates a new
                                s3 Bucket.
                                ----------------------
                                '''),
    epilog='''
        BigManSoftware Copyright 2017 - BigmanSoftware
        Developed by : Tony McClay
        Date: 7/24/2017 
        All Rights reserved''')

parser.add_argument("bucketName", help="The name of the S3 Bucket to create")
parser.add_argument("--location", help="The Location of the S3 Bucket",
                    default='us-east-2',
                    )
# parser.add_argument("--acl", help="The Access control List",
#                     default='private',
#                     choices=['private','public-read','public-read-write','authenticated-read']
#                     )


args = parser.parse_args()

print(args)
bucketName = args.bucketName
location = args.location
programName = parser.prog
# acl = args.acl

print("amazon aws Bucket Name : " + bucketName)


import boto3

s3 = boto3.client('s3')
response = s3.create_bucket(Bucket=bucketName,
                 CreateBucketConfiguration={
                     'LocationConstraint': location
                 }

                 )

print(response['Location'])
print("created")



