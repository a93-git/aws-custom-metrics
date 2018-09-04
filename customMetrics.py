"""Send custom metric data to cloudwatch
TODO: Add more details in the header
TODO: Add usage
"""

# Constants used in the program
DISK_METRIC = "DiskUtil"
MEM_METRIC = "MemUtil"
NAMESPACE = "Boto/Metric"
UNIT_MEM = 'Percent'
UNIT_DISK = 'Percent'

from datetime import datetime
import subprocess
import boto3
import os
import time

currentDir = os.getcwd()
instanceIdPath = currentDir + '/instance-id'
instanceScript = "source " + currentDir + '/instanceid.sh'
memStatPath = currentDir + '/mem-stat'
memStatScript = "source " + currentDir + '/memstat.sh'

diskStatPath = currentDir + '/disk-stat'
diskStatScript = "source " + currentDir + '/disk.sh'

subprocess.call(instanceScript, shell=True)
try:
    with open(instanceIdPath, 'r') as f:
        INSTANCE_ID = f.readline()
except:
    print('Error here')    

# Retrieve the current timestamp
try:
    timestamp = datetime.timestamp(datetime.now())
except AttributeError:
    timestamp = time.mktime(datetime.now().timetuple())

cloudwatch_client = boto3.client('cloudwatch')

def put_mem_metric_data():
    """ Sends memory metric data to cloudwatch """
    subprocess.call(memStatScript, shell=True)
    
    try:
        with open(memStatPath, 'r') as f:
            mem_value = f.readline()
    except:
        print('Error memstat')

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
                'Value': float(mem_value),
                'Unit': UNIT_MEM,
                'StorageResolution': 60
            }   
        ]
    )

put_mem_metric_data()

def put_disk_metric_data(mountpoint, disk_value):
    """ Sends disk metric data to cloudwatach """
    response = cloudwatch_client.put_metric_data(
        Namespace=NAMESPACE,
        MetricData=[
            {
                'MetricName': DISK_METRIC,
                'Dimensions': [
                    {
                        'Name': 'InstanceId',
                        'Value': INSTANCE_ID
                    },
                    {
                        'Name': 'Mountpoint',
                        'Value': mountpoint
                    }           
                ],
                'Timestamp': timestamp,
                'Value': float(disk_value),
                'Unit': UNIT_DISK,
                'StorageResolution': 60
            }
        ]
    )
    

def startDisk():
    subprocess.call(diskStatScript, shell=True)
    temp = []
    with open(diskStatPath, 'r') as f:
        for i in f.readlines():
            temp.append(i)

    for i in temp:
        try:
            z = i.strip().split(sep='\t')
        except TypeError:
            z = i.strip().split("\t")
        put_disk_metric_data(z[1], z[0])

startDisk()
