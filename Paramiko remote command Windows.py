import paramiko

# Set up the SSH client
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the server
def connect_to_server(hostname, username, password):
  ssh.connect(hostname=hostname, username=username, password=password)

# Execute the command
def execute_command(command):
  stdin, stdout, stderr = ssh.exec_command(command)

  # Print the output of the command
  for line in stdout:
    print(line)

# Close the connection
def close_connection():
  ssh.close()

# Prompt the user for the hostname, username, and password
hostname = input("Enter the hostname: ")
username = input("Enter the username: ")
password = input("Enter the password: ")

# Connect to the server
connect_to_server(hostname, username, password)

# Prompt the user for the command to execute
command = input("Enter the command to execute: ")

# Execute the command
execute_command(command)

# Close the connection
close_connection()
