"""Send custom metric data to cloudwatch
TODO: Add more details in the header
TODO: Add usage
"""

# Constants used in the program
DISK_METRIC = "DiskUtil"
MEM_METRIC = "MemUtil"
NAMESPACE = "Boto/Metric"
UNIT_MEM = 'Percent'

with open('instance-id' as f):
    INSTANCE_ID = f.readline()

from datetime import datetime
import subprocess

# Retrieve the current timestamp
timestamp = datetime.timestamp(datetime.now())

def put_mem_metric_data():
    """ Sends memory metric data to cloudwatch """
    response = client.put_metric_data(
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


