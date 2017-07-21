__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/20/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3


# Let's use Amazon S3
s3 = boto3.resource('s3')

# Upload a new file
data = open('/Users/anthonymcclay/Pictures/nielsen1.jpg', 'rb')
s3.Bucket('bigmansoftware-images').put_object(Key='nielsen1.jpg', Body=data)


