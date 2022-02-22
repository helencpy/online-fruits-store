# Script that will run in the background to monitor some of your system statistics: CPU usage, disk space, available memory and name resolution. This Python script should send an email if there are problems, such as:
# Report an error if CPU usage is over 80%
# Report an error if available disk space is lower than 20%
# Report an error if available memory is less than 500MB
# Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"

#!/usr/bin/env python3

import shutil
import psutil
import socket
import sys
import os
import emails

def check_disk_usage(disk):
    """Report an error if available disk space is lower than 20%"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free < 20
	
def check_cpu_usage():
    """Report an error if CPU usage is over 80%"""
    usage = psutil.cpu_percent(1)
    return usage > 80

def check_localhost():
    """Report an error if the hostname "localhost" cannot be resolved to 127.0.0.1"""
    localhost = socket.gethostbyname('localhost')
    if localhost == "127.0.0.1":
        return False
    else:
        return True

def check_available_memory():
    """Report an error if available memory is less than 500MB"""
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory < 500


def main(argv):	
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."
    subject = ""
    if check_cpu_usage():	    
        subject = "Error - CPU usage is over 80%"
    elif check_disk_usage('/'):
        subject = "Error - Available disk space is less than 20%"
    elif check_available_memory():
        subject = "Error - Available memory is less than 500MB"
    elif check_localhost():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
    if subject != "":	
        message = emails.generate(sender, receiver, subject, body, "")
        emails.send(message)
		
if __name__ == "__main__":
    main(sys.argv)