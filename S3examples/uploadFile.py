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
                                Uploads a file to an
                                Amazon s3 bucket 
                                ----------------------
                                '''),
    epilog='''
        BigManSoftware Copyright 2017 - BigmanSoftware
        Developed by : Tony McClay
        Date: 7/24/2017 
        All Rights reserved''')

parser.add_argument("bucketName", help="The name of the S3 Bucket to create")
parser.add_argument("fileName", help="The name file to upload")

args = parser.parse_args()
bucketName = args.bucketName
fileName = args.fileName
programName = parser.prog


# print ("aws bucket name : " + bucketName)
# print("file to upload : " + fileName)

import os,sys

def uploadFile(fileName):

    print("---------------------------------")
    print("aws bucket name : " + bucketName)
    print("file to upload : " + fileName)

    (head, tail) = os.path.split(fileName)
    # print(head + " - " + tail)
    s3 = boto3.client('s3')

    with open(fileName, 'rb') as data:
        s3.upload_fileobj(data, bucketName, tail)


    print("Completed")



uploadFile(fileName)


