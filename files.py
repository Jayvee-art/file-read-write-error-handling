def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nOriginal content read successfully.\n")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return
    except IOError:
        print(f"Error: Cannot read the file '{filename}'.")
        return

    # Modify the content — for example, convert it to uppercase
    modified_content = content.upper()

    # Define the output filename
    output_filename = "modified_" + filename

    try:
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"\nModified content written to '{output_filename}'.")
    except IOError:
        print(f"Error: Cannot write to file '{output_filename}'.")

# Run the function
read_and_modify_file()
