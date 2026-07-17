# ## Task 8: String Methods and Manipulation

# Python strings are immutable sequences of text.

# When you call a method on a string, it never modifies the original string, instead it always returns a new string with the changes applied.

# ##### 1. Case Conversions

# Methods used to quickly modify the cases of a text string.

#     .upper(): Converts all characters to uppercase.

#     .lower(): Converts all characters to lowercase.

#     .title(): Capitalizes the first letter of every word.

#     .capitalize(): Capitalizes only the very first letter of the string.

#Original String
text = "My NAME Is HaRsh"

# .upper() : Everything becomes capital letters
print(f"Original: {text}\n")
print(f"Upper Text: {text.upper()}\n")

# .lower() : Everything becomes lowercase letters
print(f"Lower Text: {text.lower()}\n")

# .title() : Capitalizes the first letter of each word
print(f"Capitalize first letter of each word : {text.title()}\n")

# .capitalize() : Capitalizes only the very first character of the whole sentence
print(f"Captilazie the first letter of sentence : {text.capitalize()}\n")

# ##### 2. Searching and Inspection

# Methods used to check the contents of a string or find specific positions.

#     .startswith(substring): Returns True if the string begins with the specified text.

#     .endswith(substring): Returns True if the string ends with the specified text.

#     .find(substring): Returns the lowest index where the substring is found, or -1 if it doesn't exist.

#     .count(substring): Counts how many times a substring appears in the text.

file = "report_2026_final.pdf"

# .startswith() : Checks the beginning of the string
print(f"File: {file}")
print(f"Does it start with 'report'? {file.startswith('report')}\n")

# .endswith() : Checks the end of the string
print(f"Does it end with '.pdf'? {file.endswith('.pdf')}\n")


phrase = "python programming python"

# .find() : Finds the first position (index) of a substring (index starts with 0)
print(f"Phrase: '{phrase}'")
print(f"Index of 'programming': {phrase.find('programming')}")
print(f"Index of 'java' (not found): {phrase.find('java')}\n")  #-1 output means 'not found'

# .count() : Counts total occurrences of a substring
print(f"How many times does 'python' appear? {phrase.count('python')}\n")

# ##### 3. Cleaning and Modification

# Methods used to trim, dissect, or alter structural parts of a string.

#     .strip(): Removes all leading and trailing whitespace (spaces, tabs, newlines).

#     .replace(old, new): Swaps all occurrences of a specific substring with a new one.

#     .split(delimiter): Breaks a string into a list of smaller strings based on a separator.

#     .join(iterable): Combines a list of strings back into a single string, using the main string as the connector.

#Raw data without cleaning
raw_data = "  apple,banana,orange  "
print(f"Original String: {raw_data}\n")

# Cleaning 
clean_data = raw_data.strip()           #remove leading and trailing whitespaces
print(f"Cleaned data (spaces removed): {clean_data}\n")

# Splitting 
fruits_list = clean_data.split(",")            # , is the delimitor (separator) here
print(f"Split data into list: {fruits_list}\n")

# Joining example
joined_text = " - ".join(fruits_list)       # - is the connector here
print(f"Joined text: {joined_text}\n")   

#replace
replaced_string = raw_data.replace('a','x')
print(f"Replaced 'a' with 'x': {replaced_string}")

# ##### 4. Character Validation

# Methods that check what kind of characters make up the string, returning a boolean (True/False).

#     .isalpha(): True if the string contains only alphabetical letters.

#     .isdigit(): True if the string contains only numeric digits.

#     .isalnum(): True if the string contains only letters and numbers (no symbols).

#Initial Strings to perform validation 
name = "Harsh"              #only alphabets
number = "99"               #only digits
name_num = "Har2s15h"       #both letters and numbers
mixed = "H@r5h"             #letters numbers and symbols

#check letters
print(f"Does name contain letters only: {name.isalpha()}")
print(f"Does name contain numbers only: {name.isdigit()}\n")


#check numbers
print(f"Does number contain letters only: {number.isalpha()}")
print(f"Does number contain numbers only: {number.isdigit()}\n")


#check numbers and letters
print(f"Does name_num contain both letters and numbers: {name_num.isalpha()}")
print(f"Does mixed contain both letters and numbers: {mixed.isdigit()}\n")
