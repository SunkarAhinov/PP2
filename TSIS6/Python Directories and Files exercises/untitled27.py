import os

# Specified path to test existence and find filename and directory
path = "/path/to/file_or_directory"

# Test if the specified path exists
if os.path.exists(path):
    print(path, "exists")

    # Find the filename and directory portion of the specified path
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print("Filename:", filename)
    print("Directory:", directory)
else:
    print(path, "does not exist")
