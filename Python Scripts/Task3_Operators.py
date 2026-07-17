# ## Task 3: Operators
# Operators are used to perform operations on variables and values.

# Types of operators in Python -

# ### 1. Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:


#Variables
'''You can change values here to see the change reflect in all operations below'''
a = 10
b = 5


#Addition
print(f"Addition: {a}+{b} = {a + b}\n")        

#Multiplication
print(f"Multiplication: {a}*{b} = {a * b}\n")

#Exponential
print(f"Exponent: {a}^{b} = {a ** b}\n")

#Division
#Division will always give float value by default  
print(f"Division: {a}/{b} = {a / b}\n")             

#Modulus (Returns the remainder after division)
print(f"Remainder: {a}/{b} = {a % b}\n")

#floor division operation
#Floor division (//) divides two numbers and rounds the result down to the nearest whole number (integer).
print(f"Floor Division: 10 // 7 = {10 // 7}")

# ## Assignment operators
# Assignment operators are used to assign values to variables:


# = : Assigns the value on the right to the variable on the left.
x = 10 
print(f"Value of x assigned: {x}\n")


# += : Adds the right value to the variable and updates the variable with the result.
x += 5 
print(f"Value of x after += 5: {x}\n")


# -= : Subtracts the right value from the variable and updates the variable with the result.
x -= 3 
print(f"Value of x after -= 3: {x}\n")


# %= : Divides the variable by the right value, finds the remainder, and updates the variable with it.
x %= 5 
print(f"Value of x after %= 5: {x}\n")


# /= : Divides the variable by the right value and updates the variable with the quotient.
x /= 2 
print(f"Value of x after /= 2: {x}\n")

# ## Comparison operators
# Comparison operators are used to compare two values:

#Comparison Operators always returns boolean result
num1 = 5
num2 = 10


print(f"{num1} > {num2} : {num1 > num2}")

print(f"{num1} < {num2} : {num1 < num2}") 

print(f"{num1} >= {num2} : {num1 >= num2}")

print(f"{num1} <= {num2} : {num1 <= num2}")

print(f"{num1} == {num2} : {num1 == num2}")

print(f"{num1} != {num2} : {num1 != num2}")

# ## Logical operators
# Logical operators are used to combine conditional statements:


#AND = Returns True if both Condtions are True
print(f"True AND True: {True and True}")
print(f"True AND False: {True and False}\n")


#OR = Returns True if at least one condition is True.
print(f"True OR False: {True or False}")
print(f"False OR False: {False or False}\n")


#NOT = Returns the opposite of the condition's boolean value.
print(f"NOT True: {not True}")
print(f"NOT False: {not False}")

# ## Ternary Operator:
# The ternary operator allows you to assign one value if a condition is true, and another if it is false:


num = 6     #try changing the value


#applying condition with if else (Ternary Operator)
'''This will return Weekend if the value of num is greater than 5, else it will return Workday and store it in day variable '''
day = "WEEKEND!" if num > 5 else "Workday!"


print(f"The day is: {day}")
