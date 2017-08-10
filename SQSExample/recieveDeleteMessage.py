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
                                    Recieve and Delete Message to a  
                                    SQS Queue
                                    ----------------------
                                    '''),
        epilog='''
            BigManSoftware Copyright 2017 - BigmanSoftware
            Developed by : Tony McClay
            Date: 7/24/2017 
            All Rights reserved''')

    parser.add_argument("queueUrl", help="The name queue URL")


    args = parser.parse_args()
    queueUrl = args.queueUrl
    programName = parser.prog
    return queueUrl, programName




def recieveDeleteMessage(queueURL):
    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    # queue_url = queueURL

    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queueURL,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']

    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=queueURL,
        ReceiptHandle=receipt_handle
    )
    print('Message Body : %s' % message['Body'])
    print('Message Attributes : %s'  % message['MessageAttributes'])
    print('Message Author : %s' % message['MessageAttributes']['Author']['StringValue'])
    print('Message Title : %s' % message['MessageAttributes']['Title']['StringValue'])


(queueURL, programName) = parseArg()
recieveDeleteMessage(queueURL)
