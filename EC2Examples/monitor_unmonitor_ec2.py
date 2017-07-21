__author__ = 'anthonymcclay'
__project__ = 'botoExamples'
__date__ = '7/20/17'
__revision__ = '$'
__revision_date__ = '$'


import sys
import boto3


ec2 = boto3.client('ec2')

state = 'ON'
if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['i-005123b8a23ddd985','i-04d63dc650b4652ff'])
    print("Monitoring on")
else:
    response = ec2.unmonitor_instances(InstanceIds=['i-005123b8a23ddd985','i-04d63dc650b4652ff'])
    print("Monitoring off")
print(response)