"""5.Write a program that opens a file, reads its contents, and writes the contents to a new file. 
Use a try-except-finally block to ensure that the file is closed even if an exception occurs during the file operations."""


def content(input_file_path, output_file_path):
    try:
        # Attempt to open the input file for reading
        with open(input_file_path, 'r') as input_file:
            # Read the content of the input file
            file_content = input_file.read()

        # Attempt to open the output file for writing
        with open(output_file_path, 'w') as output_file:
            # Write the content to the new file
            output_file.write(file_content)

    except Exception as e:
        # Handle any exceptions that may occur during file operations
        print(f"Error: {e}")

    finally:
        
        if 'input_file' in locals() and not input_file.closed:
            input_file.close()

        if 'output_file' in locals() and not output_file.closed:
            output_file.close()


input_file = 'example.txt' 
output_file = 'sample.txt' 

content(input_file, output_file)
