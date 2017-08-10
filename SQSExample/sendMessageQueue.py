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
                                    Sends a Message to a  
                                    SQS Queue
                                    ----------------------
                                    '''),
        epilog='''
            BigManSoftware Copyright 2017 - BigmanSoftware
            Developed by : Tony McClay
            Date: 7/24/2017 
            All Rights reserved''')

    parser.add_argument("queueUrl", help="The name queue URL")
    parser.add_argument("message", help="The message to send")

    args = parser.parse_args()
    queueUrl = args.queueUrl
    message = args.message
    programName = parser.prog
    return queueUrl, message, programName





def sendMessageQueue(queueURL, message):
    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    # queue_url = 'SQS_QUEUE_URL'

    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queueURL,
        DelaySeconds=10,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'The Whistler'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'John Grisham'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody=message
    )

    print("Message ID : " + response['MessageId'])



(queueURL, message, programName) = parseArg()
sendMessageQueue(queueURL, message)
