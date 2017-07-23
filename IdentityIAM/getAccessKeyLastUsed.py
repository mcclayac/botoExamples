__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/23/17'
__revision__ = '$'
__revision_date__ = '$'



import boto3
import sys
import logging


# import logging
import logging.handlers

applicationName = sys.argv[0]
logFileName = applicationName + ".log"

logger = logging.getLogger("")
logger.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(
    logFileName, maxBytes=(1048576*5), backupCount=7
)
formatter = logging.Formatter("%(asctime)s - %(process)d - %(name)s - %(filename)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


# Create IAM client
iam = boto3.client('iam')
accessKeyID = sys.argv[1]

print("aws get Access Key Last Used")
print("Access Key ID :" + accessKeyID)

logging.info('----------------------------------')
logging.info('aws get Access Key Last Used')
logging.info('Access Key ID :' + accessKeyID)
logging.info('----------------------------------')

# logging.debug("This is a debug Level")
# logging.info("This is a info Level")
# logging.warning("This is a warning Level")
# logging.error("This is an error level")
# logging.critical("This is a critical Level")
#
# logging.warning('%s before you %s', 'Look', 'leap!')
# logging.info("Tony #2")

# Get last use of access key
response = iam.get_access_key_last_used(
    AccessKeyId=accessKeyID
)

# print(response['AccessKeyLastUsed'])
region = response['AccessKeyLastUsed']['Region']
usedTime = str(response['AccessKeyLastUsed']['LastUsedDate'])

print("--------------------------------)")
print("Last used Region :\t" + region)
print("last Used Time :\t" + usedTime)

logging.info('----------------------------------')
logging.info('Last used Region :\t' + region)
logging.info("last Used Time :\t" + usedTime)
logging.info("Application Complete")
logging.info('----------------------------------')

