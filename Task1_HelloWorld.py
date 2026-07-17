# ## Task 1: Print 'Hello World'

# ##### Print is a bult-in function used to display output on console.

print("Hello World")

# ##### print: Outputs a static string or the value of an object exactly as it is.
# ##### f-string: An f-string allows you to dynamically insert variables or expressions inside the string using {}.

#set a variable
user = "Harsh"
status = "Success"

#print only prints static value
print("Hello, user")  # Output: Hello, name

#f-string displays dynamic data, so even if the values change, the output remains valid.
print(f"Hello, {user}, You status is: {status}")  # Output: Hello, Harsh
