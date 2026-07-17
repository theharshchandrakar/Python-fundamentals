# ## Task 12: Errors and Exceptions
# There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.

# #### 1. Syntax Errors
# A Syntax Error happens before Python even attempts to run your code. It means you broke the grammatical rules of the Python language. Python looks at the code, gets confused, and refuses to execute anything.

# #❌ SyntaxError: forgot the colon at the end of the if statement

# if 5 > 3

# print("Hello")

# #### 2. Exceptions (Runtime Errors)
# An Exception happens when your syntax is 100% correct, but an error occurs while the program is actually running.
# This usually happens because of unexpected data or environment issues.

# Common Built-in Exceptions:
# - ZeroDivisionError: Trying to divide a number by zero ($5 / 0$).
# - ValueError: Passing an argument with the right type but an inappropriate value (e.g., trying to turn the string "apple" into an integer: int("apple")).
# - TypeError: Trying to combine incompatible types (e.g., adding a string and an integer: "apple" + 5).
# - FileNotFoundError: Trying to open a file that doesn't exist.

# #### 3. How to Handle Exceptions (try-except)

# If an exception occurs and you don't handle it, your program crashes completely. To prevent this, Python uses a try-except block to catch errors gracefully.

# You can expand your error handling with two optional tools:

#     else: Code inside this block runs only if no errors occurred in the try block.

#     finally: Code inside this block always runs, whether an error happened or not.

# #### 1. Handling Value Error
# This program asks the user to enter their age and if they type an invalid age, it displays an error message instead of crashing.

#try block consist of code that may throw error
try:
    # age = int(input("Enter your age: "))
    age = 25  # Default value for testing
except ValueError as ve:
    print(f"Please enter a valid number! ")
else:
    print("Input Validated!")
finally:
    print("This code has exited. Run Again!")

# #### 2. Handling Index Error
# This program will display error message instead of throwing error when tried to acces invalid index.

#input list
sample_list = ["apple","banana","carara","beabadoobie"]

#accessing element of the list
try:
    # idx = int(input("Please enter the element no to be accessed: "))
    idx = 2  # Default value for testing
    print(f"The item no.{idx} is {sample_list[idx-1]}")     #fetches the item if the input is valid
except ValueError as ve:
    print("Please enter an index number!")                      #diplays message when input is not a number
except IndexError as ie:
    print("Item no is not available. Try again!")           #diplays message when input is not in list index

# #### 3. Handling Divide-by-Zero Error

# This program will display an error message instead of throwing an error when a user tries to divide a number by zero.
# Python


# input numbers
numerator = 100

# performing division operation
try:
    # denominator = int(input("Please enter a number to divide 100 by: "))
    denominator = 5  # Default value for testing
    result = numerator / denominator
    print(f"The result of division is {result}")               # displays the result if input is valid
    
except ValueError as ve:
    print("Please enter a valid integer number!")              # displays message when input is not a number
    
except ZeroDivisionError as zde:
    print("Division by zero is not allowed. Try again!")       # displays message when denominator is 0.

# #### 4. Handling File Not Found Error

# This program will display an error message instead of throwing an error when it tries to open a file that does not exist on the computer.
# Python

# target file name
filename = "unknown_file.txt"

# attempting to read the file
try:
    with open(filename, "r") as file:
        content = file.read()
        print("File contents:")
        print(content)                                         # displays file content if the file exists
        
except FileNotFoundError as fnfe:
    print(f"The file '{filename}' was not found. Try again!")  # displays message when file does not exist
