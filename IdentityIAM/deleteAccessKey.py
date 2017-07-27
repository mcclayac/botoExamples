__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/24/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3
import argparse
import textwrap

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
                                This program will Delete The IAM
                                Access key from an IAM User
                                ----------------------
                                '''),
    epilog='''
        BigManSoftware Copyright 2017 - BigmanSoftware
        Developed by : Tony McClay
        Date: 7/24/2017 
        All Rights reserved''')

parser.add_argument("iamUser", help="The IAM User to delete the key from")
parser.add_argument("accessKey", help="This is the IAM Access key to be deleted")
args = parser.parse_args()

programName = parser.prog
iamUser = args.iamUser
accessKey = args.accessKey


# Set up Logger
import logging.handlers

applicationName = programName
logFileName = applicationName + ".log"

logger = logging.getLogger(programName)
logger.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(
    logFileName, maxBytes=(1048576*5), backupCount=7
)
formatter = logging.Formatter("%(asctime)s - %(process)d - %(name)s - %(filename)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logging.info(programName)
logging.info("iam User : " + iamUser)
logging.info("Access Key : " + accessKey)


print(programName)
print("iam User : " + iamUser)
print("Access Key : " + accessKey)


# Create IAM client
iam = boto3.client('iam')

# Delete access key
iam.delete_access_key(
    AccessKeyId=accessKey,
    UserName=iamUser
)

logging.info("iam Key DELETED : " + accessKey)
print("iam Key - DELETED  : " + accessKey)

