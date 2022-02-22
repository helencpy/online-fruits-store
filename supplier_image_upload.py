# Take the jpeg images from the supplier-data/images directory that have processed previously and uploads them to the web server fruit catalog.

#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
directory = 'supplier-data/images/'

# iterate over files in
# that directory
for filename in os.listdir(directory):
  f = os.path.join(directory, filename)
  # checking if it is a file
  if os.path.isfile(f) and not filename.startswith('.') and filename.endswith('.jpeg'):
    with open(f, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
