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
                                    Deletes bucket 
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



def deleteBecketPolicy(bucketName):
    import boto3

    # Create an S3 client
    s3 = boto3.client('s3')

    # Call S3 to delete the policy for the given bucket
    s3.delete_bucket_policy(Bucket=bucketName)


(bucketName, programName) = parseArg()
deleteBecketPolicy(bucketName)



