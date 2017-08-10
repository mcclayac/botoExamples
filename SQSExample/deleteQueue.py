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
                                    Deletes an SQS Queue 
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




def deleteQueue(queueUrl):
    import boto3

    # Create SQS client
    sqs = boto3.client('sqs')

    # Delete SQS queue
    sqs.delete_queue(QueueUrl=queueUrl)

(queueUrl, programNAme) = parseArg()
deleteQueue(queueUrl)



