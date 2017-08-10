__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/27/17'
__revision__ = '$'
__revision_date__ = '$'


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
                                    Update an attribute
                                    age of a userName 
                                    ----------------------
                                    '''),
        epilog='''
            BigManSoftware Copyright 2017 - BigmanSoftware
            Developed by : Tony McClay
            Date: 7/24/2017 
            All Rights reserved''')

    parser.add_argument("tableName", help="The name table to create")
    parser.add_argument("userName", help="The userName")
    parser.add_argument("lastName", help="The lastName")
    parser.add_argument("age", help="The age ", type=int)

    args = parser.parse_args()
    tableName = args.tableName
    userName = args.userName
    lastName = args.lastName
    age = args.age
    programName = parser.prog
    return tableName, userName, lastName, age, programName



def userDynamoDBTable(tableName, userName, lastName, age):
    import boto3

    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Instantiate a table resource object without actually
    # creating a DynamoDB table. Note that the attributes of this table
    # are lazy-loaded: a request is not made nor are the attribute
    # values populated until the attributes
    # on the table resource are accessed or its load() method is called.
    table = dynamodb.Table(tableName)


    table.update_item(
        Key={
            'username': userName,
            'last_name': lastName
        },
        UpdateExpression='SET age = :val1',
        ExpressionAttributeValues={
            ':val1': age
        }
    )



(tableName, userName, lastName, age, programName) = parseArg()
userDynamoDBTable(tableName, userName, lastName, age)

