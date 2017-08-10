__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/27/17'
__revision__ = '$'
__revision_date__ = '$'





def parseArg():
    import argparse
    import textwrap

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                                    Gets a bucket 
                                    Policy
                                    ----------------------
                                    '''),
        epilog='''
            BigManSoftware Copyright 2017 - BigmanSoftware
            Developed by : Tony McClay
            Date: 7/24/2017 
            All Rights reserved''')

    parser.add_argument("bucketName", help="The name of the S3 Bucket policy")

    args = parser.parse_args()
    bucketName = args.bucketName
    programName = parser.prog
    return bucketName, programName



def getBucketPolicy(bucketName):
    import boto3
    import pprint
    pp = pprint.PrettyPrinter()

    # Create an S3 client
    s3 = boto3.client('s3')

    # Call to S3 to retrieve the policy for the given bucket
    result = s3.get_bucket_policy(Bucket=bucketName)
    pp.pprint(result['Policy'])





(bucketName, programName) = parseArg()
getBucketPolicy(bucketName)

