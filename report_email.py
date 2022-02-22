# Generate a PDF file to send to the supplier, indicating that the data was correctly processed. 

#!/usr/bin/env python3

import os
import requests
import datetime
import reports
import sys
import emails

def generate_pdf():
  # assign directory
  directory = 'supplier-data/descriptions/'
  text_data = "" 
  # iterate over files in that directory
  for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    params = {}
    # checking if it is a file
    if os.path.isfile(f):
      with open(f) as fp:
        Lines = fp.readlines()
        text_data = text_data + "name: " + Lines[0].strip() + "<br/>weight:" + Lines[1].strip() + "<br/><br/>"
  title = "Processed Update on "+ datetime.date.today().strftime("%B %d, %Y")
  reports.generate("/tmp/processed.pdf", title, text_data)

def main(argv):
  generate_pdf()
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send(message)
  
if __name__ == "__main__":
  main(sys.argv)
