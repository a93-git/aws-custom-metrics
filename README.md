# aws-custom-metrics
Send metric data for Disk and Memory

## Usage
1. Download the repo
2. Extract the contents in a folder
3. Add the following entry in crontab:
#### */5 * * * * /usr/bin/python3 /home/ec2-user/customMetrics.py
