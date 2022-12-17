"""
Check exit code:

import os

command = f"net user Guest"

result = os.system(command)
print(result)
Output: 2
"""

import os

username = input("Enter the username: ")
# Check if the user already exists
command = f"net user {username}"
result = os.system(command)
if result == 2:
  password = input("Enter the password: ")
  # The user does not exist, so create it
  command = f"net user {username} {password} /add"
  os.system(command)
else:
  print("The user already exists.")