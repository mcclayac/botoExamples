__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/24/17'
__revision__ = '$'
__revision_date__ = '$'


import boto3
import argparse
import textwrap

# Create IAM client
iam = boto3.client('iam')



parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
                                This program get a 
                                Server Certificate from the Cert Manager
                                ----------------------
                                '''),
    epilog='''
        BigManSoftware Copyright 2017 - BigmanSoftware
        Developed by : Tony McClay
        Date: 7/24/2017 
        All Rights reserved''')

parser.add_argument("cert", help="This is the Name of the Cirtificate")
args = parser.parse_args()

print(args)
programName = parser.prog
certName = args.cert


print(programName)
print("create cirtifcate name : " + certName)



# Get the server certificate
response = iam.get_server_certificate(ServerCertificateName=certName)
print(response['ServerCertificate'])

print("---------------------------------")
print("created cirtifcate name : " + certName)