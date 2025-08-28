# python-file-exception-handling-assignment
# File Handling and Exception Handling Assignment  

## 📖 Overview  
This program is a demonstration of file handling and exception handling in Python. It is designed to show how a program can safely read from files, modify their contents, and write the results to new files while accounting for possible errors. The main goal is to ensure the program remains stable and user-friendly even when things go wrong, such as when a file is missing or inaccessible.  

When executed, the program prompts the user to enter the name of a file they want to process. It then attempts to open the file and read its contents. If the file is found and can be read successfully, the program converts all of its text into uppercase letters. The modified version of the content is then saved into a new file that is automatically created with the prefix `modified_` added to the original filename.  

If the file cannot be opened, the program does not crash. Instead, it gracefully handles errors such as missing files (`FileNotFoundError`) or read/write issues (`IOError`). In these cases, it displays a clear message to the user explaining what went wrong and confirms that file processing has been aborted. If everything works correctly, the program provides confirmation that the new modified file has been created successfully.  

This assignment highlights two important concepts:  
1. **File I/O** — how to open, read, modify, and write files in Python.  
2. **Error Handling** — how to anticipate problems and ensure the program communicates clearly with the user rather than failing unexpectedly.  

By combining these two aspects, the program shows how to write more reliable and user-friendly Python code.  
