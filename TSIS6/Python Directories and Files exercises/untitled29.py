# Specified list to write to file
my_list = ["apple", "banana", "cherry", "date"]

# Specified file to write the list
filename = "path/to/output_file.txt"

# Open the specified file in write mode
with open(filename, "w") as file:
    # Use a loop to write each element of the list to the file
    for element in my_list:
        file.write(element + "\n")

# Print a message indicating that the list has been written to the file
print("The list has been written to", filename)
