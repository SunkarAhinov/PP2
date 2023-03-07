# Specified text file to count lines
filename = "path/to/text_file.txt"

# Open the specified text file in read mode
with open(filename, "r") as file:
    # Use a loop to iterate through each line in the file and count the number of lines
    num_lines = 0
    for line in file:
        num_lines += 1

# Print the number of lines in the file
print("Number of lines in", filename, ":", num_lines)
