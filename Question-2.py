"""2.Create a program that opens a file and reads its contents. 
Use a try-except block to handle the FileNotFoundError exception and display a custom error message if the file does not exist."""

class FileReader:
    def __init__(self):
        # Initialize the class with a None file path
        self.file_path = None

    def get_file_path(self):
        # Prompt the user to enter the file path and assign it to self.file_path
        self.file_path = input("Enter the file path: ")

    def read_file(self):
        try:
            # Attempt to open the file for reading
            with open(self.file_path, 'r') as file:
                # Read the content of the file
                content = file.read()
                # Display the file contents to the user
                print("File contents:")
                print(content)
                # Return the content
                return content
        except FileNotFoundError:
            # Handle the case where the file is not found
            print(f"The file '{self.file_path}' does not exist.\nCreating a new file.........")
            return None
        except Exception as e:
            # Handle unexpected errors and print an error message
            print(f"Error: An unexpected error occurred - {e}")
            return None

    def create_or_append_file(self, content):
        try:
            # Attempt to open the file for appending or writing
            with open(self.file_path, 'a' if content else 'w') as file:
                if content:
                    # If content exists, indicate that content is being appended
                    print("Appending content to the file.")
                else:
                    # If no content exists, indicate that a new file is created
                    print("New file created.")
                # Prompt the user to enter new content
                new_content = input("Enter content to add (or press Enter to skip): ")
                if new_content:
                    # If new content is provided, write it to the file
                    file.write(new_content + '\n')
        except Exception as e:
            # Handle unexpected errors during file creation or appending
            print(f"Error: Unable to create or append to the file - {e}")

# Create an instance of the FileReader class
file_reader = FileReader()

# Get user input for the file path
file_reader.get_file_path()

# Read the file and get its content
file_content = file_reader.read_file()


file_reader.create_or_append_file(file_content)





