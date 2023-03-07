# Import the string module to get the alphabet
import string

# Loop through each letter of the alphabet
for letter in string.ascii_uppercase:
    # Generate the filename for the current letter
    filename = letter + ".txt"
    # Open the file in write mode
    with open(filename, "w") as file:
        # Write some text to the file
        file.write("This is the file for the letter " + letter)
    # Print a message indicating that the file has been created
    print("File", filename, "created.")
