# ## Task 2: 5 Variable Excercises

# ##### 1. Variables: Variables are containers used to store data values in a program.

#Declaring a Variable
name = "Harsh"
num = 56
numlist = [1,2,3,4,5]

#printing the values of variables
print(f"{name}, {num}, {numlist}")

# ##### 2. Data Types: In python, we dont need to declare data type, python infers it automatically.


#Declaring Variables without specifying data types
name = "Harsh"
number = 99
number2 = 36.68
arraylist = [1,2,3,4,5]


#type() function is used to display the data type of the provided value. 
print(f"""
Data type of {name} = {type(name)} \n
Data type of {number} = {type(number)} \n
Data type of {number2} = {type(number2)} \n
Data type of {arraylist} = {type(arraylist)} \n""")

# #### 3. Type-casting: Type casting is the process of converting a value from one data type to another.
# There are two types of Type Casting
# -  Implicit - Python automatically converts one data type to another when it is safe to do so, typically to prevent data loss.
# - Explicit - You manually convert data using built-in functions like int(), float(), or str(). Data can be lost here.

#Implicit Type-Casting

#Integer is automatically converted to float
num_int = 10        #integer
num_float = 10.5    #float

#Adding the variable values
result = num_int + num_float 

#Printing result and its data type
print(f"Result: {result}") 
print(f"Data Type: {type(result)}")

#Explicit Type-Casting

# Converting string to integer
age_string = "25"               #string type
age_int = int(age_string)       #explicit casting
print(f"converted string type to: {type(age_int)}")

# Converting number to string
price = 100                     #int type
price_str = str(price)          #explicit casting
print(f"converted int ring type to: {type(age_int)}")

'''Explicit Type-Casting may result in data loss primarily when converting from a "larger" or more complex type to a "smaller" or simpler one.'''

#Float to Integer Casting
num1 = 26.85        #Float Value
num2 = int(num1)    #Casting to Integer value


print(num2)
#output = 26 (0.85 is lost)

'''String to Number (Failure): If you try to cast a string that contains non-numeric characters 
(like "10abc") to an int, it will crash with a ValueError.'''

strvalue = "Harsh"       #String Value
try:
    numvalue = int(strvalue) #Casting to Integer
    print(numvalue)
except ValueError as ve:
    print(f"ValueError: {ve}")
    print("Note: Cannot convert a non-numeric string to integer.")

#Note: running this cell will result in an error.

# #### 4. Boolean Values:
# Boolean values represent one of two logical states: True or False

#Assigning Boolean Value
bool_value = True

#print its data type
print(f"Data type: {type(bool_value)}")


# Operations like 10 > 5 return a boolean result

#result of comparison operators is always in Boolean.
print(5>4)          # Asks if 5 is greater than 4, and print its Result

# #### 5. Dynamic Values:
# Python allows this because it is a dynamically typed language, meaning the data type of a variable is determined at runtime based on the value assigned to it.

# Assign a string
'''We assign a String Value to a variable and print its type'''
var = "Harsh"
print(f"Value: {var}, Type: {type(var)}")

# Re-assign to an integer
'''We assign an Integer Value to the same variable and print its type'''
var = 56
print(f"Value: {var}, Type: {type(var)}")

# The result show two different data types when run, showing that the code is dynamically executed while running.
