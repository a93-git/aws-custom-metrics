"""Send custom metric data to cloudwatch
TODO: Add more details in the header
TODO: Add usage
"""

# Constants used in the program
DISK_METRIC = "DiskUtil"
MEM_METRIC = "MemUtil"
NAMESPACE = "Boto/Metric"
UNIT_MEM = 'Percent'

from datetime import datetime
import subprocess
import boto3

subprocess.call("instanceid.sh")

with open('instance-id', 'r') as f:
    INSTANCE_ID = f.readline()

# Retrieve the current timestamp
timestamp = datetime.timestamp(datetime.now())

cloudwatch_client = boto3.client('cloudwatch')

def put_mem_metric_data():
    """ Sends memory metric data to cloudwatch """
    response = cloudwatch_client.put_metric_data(
        Namespace=NAMESPACE,
        MetricData=[
            {
                'MetricName': MEM_METRIC,
                'Dimensions': [
                    {
                        'Name': 'InstanceId',
                        'Value': INSTANCE_ID
                    }
                ],
                'Timestamp': timestamp,
                'Value': 
                'Unit': UNIT_MEM,
                'StorageResolution': 60
            }
        ]
    )


