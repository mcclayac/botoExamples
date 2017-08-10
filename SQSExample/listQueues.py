__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/20/17'
__revision__ = '$'
__revision_date__ = '$'





import boto3


# Get the service resource
sqs = boto3.resource('sqs')

# Print out each queue name, which is part of its ARN
for queue in sqs.queues.all():
    print("queueArn : " + queue.attributes['QueueArn'].split(':')[-1] + "\t queue URL : " + queue.url )




