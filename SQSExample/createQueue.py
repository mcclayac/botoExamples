__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/20/17'
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




def createQueue(queueName):
    import boto3

    # Get the service resource
    sqs = boto3.resource('sqs')

    # Create the queue. This returns an SQS.Queue instance
    queue = sqs.create_queue(QueueName=queueName, Attributes={'DelaySeconds': '5'})

    # You can now access identifiers and attributes
    print(queue.url)
    print("Delay Seconds : " + queue.attributes.get('DelaySeconds'))



(queueName, programName) = parseArg()
createQueue(queueName)



