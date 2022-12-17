import os
path= 'C:\\Users\\xx\\'
if os.path.isdir(path):
  print("It is a directory")
elif os.path.isfile(path):
  print ("it is a file")
else:
  print("Does not exist")