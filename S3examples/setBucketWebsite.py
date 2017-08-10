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
                                    Sets a bucket 
                                    Website
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


def setBucketWebsite(bucketName):
    import boto3

    # Create an S3 client
    s3 = boto3.client('s3')

    # Create the configuration for the website
    website_configuration = {
        'ErrorDocument': {'Key': 'error.html'},
        'IndexDocument': {'Suffix': 'index.html'},
    }

    # Set the new policy on the selected bucket
    response = s3.put_bucket_website(
        Bucket=bucketName,
        WebsiteConfiguration=website_configuration
    )

    print(response)


(bucketName, programName) = parseArg()
setBucketWebsite(bucketName)

