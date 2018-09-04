# aws-custom-metrics

## What?
Create metrics for and send metric data for disk space utilization and memory
utilization of AWS EC2 instances running Linux


## How?
It retrieves the:
1. <em>Instance id</em> from the instance metadata
2. <em>memory utilization</em> from <em>/proc/meminfo</em> file
3. <em>disk space utilization</em> information from <em>df -h</em> output



## Requirements
- Python 2.7+ or Python 3.x
- Boto3 library



## Usage
1. Check the current python version
<pre><code>python -V</pre></code>
2. Check Boto 3 is installed
<pre><code>python -m boto3</pre></code>
* Above command should give an error like below
![Alt erroMessage](https://github.com/a93-git/aws-custom-metrics/blob/master/boto3Error.png)
3. Clone the repo in your local directory
4. Copy the contents to home directory of current user
5. Add the following entry in crontab:
<pre><code>*/5 * * * * /path/to/python/executable /home/[username]/customMetrics.py</pre></code>

## Resources
1. <a
href="https://awc.com.my/uploadnew/5ffbd639c5e6eccea359cb1453a02bed_Setting%20Up%20Cron%20Job%20Using%20crontab.pdf">How
to add a cron job</a>
2. <a href="https://help.github.com/articles/cloning-a-repository/">How to
clone a github repo </a>
3. <a
href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html">Boto
3 documentation</a>

