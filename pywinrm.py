import argparse
import winrm

# Use the argparse module to parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("hostname")
parser.add_argument("username")
parser.add_argument("password")
args = parser.parse_args()

# Set up the RDP session using the values from the command line arguments
session = winrm.Session(
    args.hostname,
    auth=(args.username, args.password)
)

# Execute the command
result = session.run_cmd("dir")

# Print the output of the command
print(result.std_out)


## python script.py windows.server.com admin password
