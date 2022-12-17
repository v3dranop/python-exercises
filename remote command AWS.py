import paramiko
import boto3

# Create a new EC2 client
ec2 = boto3.client("ec2")

# Retrieve the hostname and authentication credentials for the EC2 instance
instance = ec2.describe_instances(InstanceIds=["i-1234567890"])
hostname = instance["Reservations"][0]["Instances"][0]["PublicDnsName"]
username = "ec2-user"
password = instance["Reservations"][0]["Instances"][0]["KeyName"]

# Create a new SSH client
ssh = paramiko.SSHClient()

# Connect to the remote server
ssh.connect(hostname=hostname, username=username, password=password)

# Execute the command
stdin, stdout, stderr = ssh.exec_command("ls -l")

# Print the output of the command
print(stdout.read().decode())

# Close the SSH client
ssh.close()