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
                                    use an DynamoDB  
                                    Table Name
                                    ----------------------
                                    '''),
        epilog='''
            BigManSoftware Copyright 2017 - BigmanSoftware
            Developed by : Tony McClay
            Date: 7/24/2017 
            All Rights reserved''')

    parser.add_argument("tableName", help="The name table to create")
    parser.add_argument("userName", help="The userName")
    parser.add_argument("firstName", help="The first name user to create")
    parser.add_argument("lastName", help="The last Name user to create")
    parser.add_argument("age", help="The age ", type=int)
    parser.add_argument("education", help="The education")


    args = parser.parse_args()
    tableName = args.tableName
    userName = args.userName
    firstName = args.firstName
    lastName = args.lastName
    age = args.age
    education = args.education
    programName = parser.prog
    return tableName, userName, firstName, lastName, age, education, programName



def userDynamoDBTable(tableName, userName, firstName, lastName, age, education):
    import boto3

    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Instantiate a table resource object without actually
    # creating a DynamoDB table. Note that the attributes of this table
    # are lazy-loaded: a request is not made nor are the attribute
    # values populated until the attributes
    # on the table resource are accessed or its load() method is called.
    table = dynamodb.Table(tableName)

    # Print out some data about the table.
    # This will cause a request to be made to DynamoDB and its attribute
    # values will be set based on the response.
    print(table.creation_date_time)

    table.put_item(
        Item={
            'username': userName,
            'first_name': firstName,
            'last_name': lastName,
            'age': age,
            'account_type': 'standard_user',
            'edducation' : education
        }
    )



(tableName, userName, firstName, lastName, age, education, programName) = parseArg()
userDynamoDBTable(tableName, userName, firstName, lastName, age, education)

