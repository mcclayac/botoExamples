import boto3


# Create IAM client
iam = boto3.client('iam')

# Get a policy
response = iam.get_policy(
    PolicyArn='arn:aws:iam::aws:policy/AWSLambdaExecute'
)
# print(response['Policy'])

policyArn = response['Policy']['Arn']
policyDescription = response['Policy']['Description']
policyName = response['Policy']['PolicyName']
policyID = response['Policy']['PolicyId']


print("Policy Name :", policyName, "\tPolicy ID:", policyID, "\tPolicy ARN :", policyArn)


