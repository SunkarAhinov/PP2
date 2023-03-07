import os

# Specified path to delete
file_path = "path/to/file.txt"

# Check if the specified path exists
if os.path.exists(file_path):
    # Check if the current user has access to the file
    if os.access(file_path, os.R_OK):
        # Delete the file
        os.remove(file_path)
        print("File deleted successfully!")
    else:
        print("You don't have read access to this file.")
else:
    print("The specified file does not exist.")
