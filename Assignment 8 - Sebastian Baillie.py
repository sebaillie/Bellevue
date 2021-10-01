 # Append data in file, separated by commas
def append_data():
    with open(filePath, 'w') as fileHandle:
        fileHandle.write(name + "," + address + "," + phone)
        fileHandle.close()

# Use OS Library
import os

# Prompt user for directory and name of file
directory = input("Please enter the directory you would like to use: ")
if directory == "":
    directory = "/home/sebastian/Desktop/School/IntroToProgramming/Week8/"
    print("Using default directory: " + directory)
fileName = input("Please enter the file name you would like to create/use: ")

# Add '/' at the end of directory if it's not there
if directory.endswith('/'):
    pass
else:
    directory = directory + "/"
    
# Removes '/' is found at beginning of fileName
if fileName.startswith('/'):
    fileName = fileName[1 : ]
else:
    pass

filePath = directory + fileName

# Validate the directory exists
if os.path.exists(directory):
    print("Found directory...")
else:
    print("Directory not found...")
    isCreated = input("Should it be created? [Y/N]")
    if isCreated.lower() == 'y' or isCreated.lower() == 'yes':
        os.mkdir(directory)
    else:
        print("Goodbye.")
        exit()

# Ask user for name, address, and phone number
name = input("Please enter your name: ")
address = input("Please enter your address: ")
phone = input("Please enter your phone number: ")

# Create file
if os.path.exists(filePath):
    print("File '" + fileName + "' found...")
    print("Writing to file...")
    append_data()
else:
    print("File not found...")
    print("Creating new file '" + fileName + "'...")
    append_data()

# Print directory and file to user
print("File path: " + filePath)

# Print contents of file to user
print("Data inside file: ")
with open(filePath, 'r') as fileHandle:
    data = fileHandle.read()
print(data)
