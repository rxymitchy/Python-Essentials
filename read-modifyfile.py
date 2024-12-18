def read_file_with_error_handling():
    filename = input("Enter the filename you want to read: ")
    
    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    
    except IOError:
        print(f"Error: There was an issue reading the file {filename}. It may not be accessible.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_file_with_error_handling()

def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (for example, convert text to uppercase)
        modified_content = content.upper()  # Modify this line to change how content is modified
        
        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File has been modified and saved as {output_filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print(f"Error: There was an issue reading or writing to the file.")

# Example usage
input_file = 'example.txt'  # Replace with your file name
output_file = 'modified_example.txt'  # The new file where the modified content will be saved

read_and_modify_file(input_file, output_file)
