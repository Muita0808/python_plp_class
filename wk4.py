def read_and_write_file():
    # Prompt the user for the input file name
    input_file = input("Enter the name of the file to read: ")
    
    try:
        # Try to open the input file for reading
        with open(input_file, "r") as infile:
            content = infile.read()
            print(f"\nOriginal Content:\n{content}\n")
            
            # Modify the content (example: adding line numbers)
            modified_content = ""
            for index, line in enumerate(content.splitlines(), start=1):
                modified_content += f"{index}: {line}\n"
            
            # Prompt the user for the output file name
            output_file = input("Enter the name of the file to write to: ")
            with open(output_file, "w") as outfile:
                outfile.write(modified_content)
            
            print(f"\nModified content written to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read/write '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_file()
