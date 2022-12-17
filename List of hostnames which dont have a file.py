#! \\fileshare\python\python.exe

import os
import socket

# Get the hostname of the computer
hostname = socket.gethostname()

# Set the path of the text file on the file share
file_share = r"\\fileshare\file.txt"
file_path = "C:\\test.txt"

# Check if the file exists
if os.path.exists(file_path):
  # The file exists, so do nothing
  pass
else:
  # The file does not exist, so create it and add the hostname
  with open(file_share, "a") as file:
    file.write(hostname  + "\n")
