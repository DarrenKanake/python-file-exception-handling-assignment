# File Handling and Exception Handling Assignment
# Part 1: File Read & Write Challenge

# 1.Ask the user for a filename.
# Example: “Enter the name of the file you want to open:”
filename = input("Enter the name of the file you want to open: ")
# 2.Try to open the file in read mode.
# check whether reading was successful.
success = False
# If it fails, show an error message.
try:
    with open(filename, 'r') as file:
        content = file.read()
        success = True
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError:
    print(f"Error: Could not read the file '{filename}'.")

# 3.Read the file’s contents into a variable.
# (Already done in the try block above)

# 4.Modify the contents somehow.
# For example, convert all text to uppercase.
# Do modification + writing only if reading was successful.
if success:
    modified_content = content.upper()
    # 5.Write the modified content to a new file.
    new_filename = "modified_" + filename
    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"Modified content written to '{new_filename}'")
    except IOError:
        print(f"Error: Could not write to the file '{new_filename}'.")
    
    # 6.Confirm to the user that it worked.
    print("File processing completed successfully.")
else:
    print("File processing could not be completed due to previous errors.")



