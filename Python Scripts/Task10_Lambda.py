# ## Task 10: Lambda Functions

# ##### Labmda Function:
# lambda function is a small, anonymous (unnamed) function in Python.

# Unlike a normal function defined with def, a lambda function is written in a single line, can take any number of arguments, but can only have one single expression as its logic.

# #### Syntax:
#     lambda arguments: expression

# ##### 1. Square Function
# This function will simply return the square of provided number.

#input number to be passed to function
num = 11

#square is the name of the function
square = lambda x: x**2

#We call the function using the function name i.e square(parameter)

print(f"Square of {num}: {square(num)}")

# ##### 2. Odd/Even check

#input number
num = 11

#Lambda function using Ternary operator
OE_check = lambda x: True if x%2 == 0 else False


#calling the function
'''result will consist of "Even" or "Odd" based on the ouput recieved from the lambda function'''
result = "Even" if OE_check(num) else "Odd"

#printing result
print(f"{num} is {result}")

# ##### map():

# Use map() when you want to apply the exact same operation to every single item in a list. It returns a new list of the exact same length, but with altered values.

# Example: Multiplying every number in a list by 2.

# #### 3. Convert list elements
# Given a list of strings representing numbers, we convert this entire list into actual integers.

#list of strings representing numbers
s_list = ["25","12","97","69","23",18.21]

'''
- lambda function is converting element of the list into integer using int().
- map() function is iterating over all the elements in the list and passing it to lambda function as an argument.
- list() function is converting the output of the map function in a list
- and we store the list in the n_list variable.
'''
n_list = list(map(lambda x:int(x),s_list))

print(n_list)
#note the float value is also converted to integer and the decimal value is lost

# ##### filter():
# Use filter() when you want to keep only the items that meet a specific condition. It tests each item with a True/False rule and throws away the ones that return False.

# Example: Keeping only the even numbers from a list.

# #### 4. Words Filter
# We will pass a list of names and will keep list of names that start with vowels (A,E,I,O,U).

#name list
name_full = ["India","Pakistan","Dubai","Iraq","Australia","Mexico","Uganda"]

#this list enables the function to check for vowels
vowels = ["A","E","I","O","U"]

#function
vowel_list = list(filter(lambda x:x[0] in vowels ,name_full))

print(vowel_list)

# ##### reduce():
# Use reduce() when you want to combine all the items in a list into one single value (like a sum, a product, or a string concantenation). It processes the list in pairs, carrying the running total forward.

# Note: You must import it using from functools import import reduce.

# Example: Multiplying all numbers together to get a single final product.

# ##### 5. Multiply all items
# Given a list of numbers we will use reduce() and a lambda function to find the total product of multiplying all the numbers together .

# if nums = [1,2,3,4] then,
# ($1 \times 2 \times 3 \times 4$).

#First, import reduce from the functools module.
from functools import reduce

#the list of numbers
num = [2,5,3,8]

#function
total_product = reduce(lambda x,y : x*y, num)

print(f"Total product of {num} is {total_product}")
