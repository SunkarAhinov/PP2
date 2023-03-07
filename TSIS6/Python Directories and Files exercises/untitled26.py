import os

# Specified path to check access
path = "/path/to/file_or_directory"

# Test if the specified path exists
if os.path.exists(path):
    print(path, "exists")

    # Test if the specified path is readable
    if os.access(path, os.R_OK):
        print(path, "is readable")
    else:
        print(path, "is not readable")

    # Test if the specified path is writable
    if os.access(path, os.W_OK):
        print(path, "is writable")
    else:
        print(path, "is not writable")

    # Test if the specified path is executable
    if os.access(path, os.X_OK):
        print(path, "is executable")
    else:
        print(path, "is not executable")
else:
    print(path, "does not exist")
