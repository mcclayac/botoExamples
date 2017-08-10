__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/27/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call to S3 to retrieve the policy for the given bucket
result = s3.get_bucket_acl(Bucket='mcclayac-bucket1')
print(result)


