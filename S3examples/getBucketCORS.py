__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/27/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3
import pprint

pp = pprint.PrettyPrinter()



def parseArg():
    import argparse
    import textwrap

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
                                    Lists a Buckets CORS
                                    Configuratiom 
                                    ----------------------
                                    '''),
        epilog='''
            BigManSoftware Copyright 2017 - BigmanSoftware
            Developed by : Tony McClay
            Date: 7/24/2017 
            All Rights reserved''')

    parser.add_argument("bucketName", help="The name of the S3 Bucket CORS")

    args = parser.parse_args()
    bucketName = args.bucketName
    programName = parser.prog
    return bucketName, programName

def getCORS_Rules(bucketName):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Call S3 to get CORS configuration for selected bucket
    result = s3.get_bucket_cors(Bucket=bucketName)
    print('-------------------------------')
    print("bucket name : " + bucketName)
    pp.pprint(result['CORSRules'])



(bucketName, programName) = parseArg()
getCORS_Rules(bucketName)





