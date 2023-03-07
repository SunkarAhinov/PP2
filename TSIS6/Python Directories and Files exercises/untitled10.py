import os

# Specified path to list directories and files
path = "/path/to/directory"

# List all directories in the specified path
print("List of directories in", path)
for dir_name in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir_name)):
        print(dir_name)

# List all files in the specified path
print("\nList of files in", path)
for file_name in os.listdir(path):
    if os.path.isfile(os.path.join(path, file_name)):
        print(file_name)

# List all directories and files in the specified path
print("\nList of all directories and files in", path)
for item_name in os.listdir(path):
    item_path = os.path.join(path, item_name)
    if os.path.isdir(item_path):
        print("[DIR]", item_name)
    elif os.path.isfile(item_path):
        print("[FILE]", item_name)