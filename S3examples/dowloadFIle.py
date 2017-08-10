__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/27/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3
import botocore


bucketName  = ""
keyName     = ""
programName = ""


def parseArgumemts():
    import argparse
    import textwrap

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                                    Downloads a file from an
                                    Amazon s3 bucket 
                                    ----------------------
                                    '''),
        epilog='''
            BigManSoftware Copyright 2017 - BigmanSoftware
            Developed by : Tony McClay
            Date: 7/24/2017 
            All Rights reserved''')

    parser.add_argument("bucketName", help="The name of the S3 Bucket to create")
    parser.add_argument("keyName", help="The S3 key")

    args = parser.parse_args()
    bucketName = args.bucketName
    keyName = args.keyName
    programName = parser.prog
    return bucketName, keyName, programName


def downloadFile(bucketName, keyName):

    s3 = boto3.resource('s3')

    try:
        s3.Bucket(bucketName).download_file(keyName, keyName)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise



(bucketName, keyName, programName) = parseArgumemts()
print("bucketName : " + bucketName)
print("S3 Key : " + keyName)
downloadFile(bucketName, keyName)





