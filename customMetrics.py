"""Send custom metric data to cloudwatch
TODO: Add more details in the header
TODO: Add usage
"""

# Constants used in the program
DISK_METRIC = "DiskUtil"
MEM_METRIC = "MemUtil"

from datetime import datetime

# Retrieve the current timestamp
timestamp = datetime.timestamp(datetime.now())
