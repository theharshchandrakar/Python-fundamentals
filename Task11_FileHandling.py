# ## Task 11: File Handling
# File handling in Python allows you to work with files stored on your computer. It enables your program to read data from a file, write new data into a file, or append (add) data to an existing file.

# #### Task 1:
#  Create the file and write the initial line (overwrites if it exists)

#when you use open to open a file, you need to explicitly close the file to prevent data leakage
import os
if os.path.exists("log.txt"):
    os.remove("log.txt")
f = open("log.txt","x")         #"x" is used to create file

print("file has been created!")
#this will give error if file already exists

f.close()                   #closing the opened file (IMPORTANT)

'''when file is opened with 'with' keyword, you dont need to explicitly close the file.'''
with open("log.txt", "w") as file:      #'w' is used when we need to overwrite the file contents
    file.write("System Initialized\n")  

#read the file to verify the write function.
with open("log.txt","r") as file:       #"r" is used to read the file
    print(file.readline())              #.readline() returns the contents until a newline or EOF

# ##### Task 2:
# Reopen the file in append mode to add a new line without erasing the content.

#"a" is used to append content to the file without replacing any contents
with open("log.txt", "a") as file:
    file.write("User logged in\n")


# Reading the file back to verify changes
with open("log.txt", "r") as file:
    print("--- log.txt Contents ---")
    print(file.read())
