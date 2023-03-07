# Specified input file to read
input_file = "path/to/input_file.txt"

# Specified output file to write
output_file = "path/to/output_file.txt"

# Open the input file in read mode and the output file in write mode
with open(input_file, "r") as input_f, open(output_file, "w") as output_f:
    # Use the read() method of the input file object to read the contents of the file
    contents = input_f.read()

    # Use the write() method of the output file object to write the contents to the file
    output_f.write(contents)

# Print a message indicating that the contents have been copied to the output file
print("The contents of", input_file, "have been copied to", output_file)
