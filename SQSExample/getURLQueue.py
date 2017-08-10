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
                                    Creates an SQS Queue 
                                    SQS Queue
                                    ----------------------
                                    '''),
        epilog='''
            BigManSoftware Copyright 2017 - BigmanSoftware
            Developed by : Tony McClay
            Date: 7/24/2017 
            All Rights reserved''')

    parser.add_argument("queueName", help="The name queue to create")

    args = parser.parse_args()
    queueName = args.queueName
    programName = parser.prog
    return queueName, programName

def getQueueURL(queueName):
    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    # Get URL for SQS queue
    response = sqs.get_queue_url(QueueName=queueName)

    print(response['QueueUrl'])

(queueName, programName) = parseArg()
getQueueURL(queueName)


