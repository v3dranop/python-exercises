import sys
import requests

# Get the URL to send the request to from the command line arguments
url = sys.argv[1]

# Make a GET request to the website
response = requests.get(url)

# Check the status code of the response
if response.status_code == 200:
  # If the status code is 200, the request was successful
  # and we can access the content of the response
  print(response.text)
else:
  # If the status code is not 200, the request was not successful
  # and we should handle the error
  print("Error: status code {}".format(response.status_code))

 ## Usage: python request.py https://www.example.com