# file-read-write-error-handling
A simple Python script to read, modify, and write files with error handling.
# File Read & Write with Error Handling 🖋️🧪

This Python script allows users to:
- Read the contents of a file,
- Modify the contents (e.g., convert to uppercase),
- Handle common file errors (like file not found or unreadable files),
- Write the modified content to a new file.

## 📂 How It Works

1. Prompts the user to enter the name of the file to read.
2. If the file exists and is readable, it reads the contents.
3. Transforms the content (e.g., to uppercase).
4. Writes the modified content to a new file prefixed with `modified_`.
5. Handles errors like:
   - `FileNotFoundError`: If the file doesn't exist.
   - `IOError`: If the file cannot be read or written.
