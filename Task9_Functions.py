# ## Task 9: Functions

# ##### Functions:
# A function in Python is a reusable block of code that only runs when it is called. It helps organize code, prevents repetition, and makes programs easier to maintain.

# ##### Key Concepts

# - Parameters & Arguments: Parameters are the variables listed in the function definition (name). Arguments are the actual values passed into the function when calling it ("Harsh").

# - Return Statement: The return keyword exits a function and passes a value back to the caller. If no return is specified, the function automatically returns None.

# - Scope: Variables created inside a function belong to that function's local scope and cannot be accessed from outside it.

# - Default: An optional parameter in a function definition that automatically assigns a fallback value if no value is provided when the function is called.

# ##### Docstring:
# A docstring (documentation string) is a special multi-line string used to explain what a function, class, or module does.

# To add a docstring, place a triple-quoted string (""") immediately below the function definition line, before any other code.

# Anyone using the function can read the docstring instantly just by hovering their mouse cursor over the function name.

# #### 1. Factorial

# The factorial of a positive integer $n$ (written as $n!$) is the product of all positive integers less than or equal to $n$.Mathematically, it looks like this:$$n! = n \times (n - 1) \times (n - 2) \times \dots \times 1$$

# This function will calculate the factorial of the provided number.

#Input integer
number = 5                  #change this input to give different values to the function


#------------------------------------------------------------------------------------------------
#Defining a function
'''"def" keyword is used to define a function and the function code blocks are written inside it'''

def factorial(n):
    """
    Calculates and returns the factorial of the provided integer n.

    Accepts 1 Parameter of non-negative Integer type: n.

    Returns Integer: Factorial result
    """
    if n<0:                     #since negative numbers dont have factorial
        return "Factorial doesnt exist for negative numbers!"
    elif n == 0 or n == 1:
        return 1                #since factorial of 0 or 1 is 1
    else:
        result = 1              #local scope (doesnt exist outside function)
        for i in range(1,n+1):
            result = result * i
        return result   
    
#----------------------------------------------------------------------------------------

#calling the function we defined
print(f"Factorial of {number}: {factorial(number)}")

# #### 2. Prime Number Check
# The LogicA prime number is a number greater than 1 that can only be divided evenly by 1 and itself. To check if a number is prime efficiently, we only need to test divisors up to the square root of the number ($\sqrt{n}$). If no factors are found by that point, none will be found at all.

# This function will check if a number is prime or not.

#Number to be checked (input)
num = 5

#------------------------------------------------------------------------------------
#Defining function
def prime_check(n):
    """
    Checks if a number is prime or not.

    Parameter: accepts 1 integer 'n'

    Output: Return Boolean value- 'True/False'
    """
    if n<=1:                #Numbers equal to or less than 1 are not prime
        return False
    elif n == 2:            #2 is the only prime number
        return True
    else:
        #check every number from 2 to n-1
        for i in range(2,n):        #upper limit is 'n' because it is exclusive in range()
            if n%i == 0:
                return False        #If its divided by any number greater than 2 and less than itself
    return True             #If the loop finishes without finding any factors yet. Its prime

#-------------------------------------------------------------------------------------------

#Formatting the output from the function
result = prime_check(num)

if result is True:
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is not a Prime number.")

# #### 3. Palindrome
# A palindrome is a word, phrase, number, or sequence of characters that reads exactly the same backward as it does forward (ignoring spaces, punctuation, and capitalization).

# Examples : "racecar" and "radar", or numbers like 121

#input
# n = input("Enter input to check for palindrome: ")
n = "racecar"  # Default value for testing

#---------------------------------------------------------------------------
#defining the function
def palindrome(n):
    """
    Checks if a word is a palindrome.
    Returns True if it reads the same backward as forward, False otherwise.
    """
    clean_text = n.lower()          #lower the cases so the checks dont fail because of it

    #[::-1] is iterating over the string from the backwards (step= -1)
    if clean_text ==  clean_text[::-1]:
        return True
    else:
        return False
#----------------------------------------------------------------------------

#Formatting the output from the function
result = palindrome(n)

if result is True:
    print(f"{n} is a Palindrome.")
else:
    print(f"{n} is not a Palindrome.")

# #### 4. Temperature Convert
# This function will convert temp in Farenheit to Celcius, using the simple math formula
# $$C = (F - 32) \times \frac{5}{9}$$
# How to use it step-by-step:

# 1. Take the Fahrenheit temperature and subtract 32.

# 1. Multiply that result by 5.

# 1. Divide the total by 9.

#input farenheit temperature
F = 100

#----------------------------------------------------------------------------------------------
#Function defintion
def F_to_C_convert(F_temp):
    C = F_temp - 32
    C *= 5/9
    return round(C,2)
#--------------------------------------------------------------------------------------------

#call function
C = F_to_C_convert(F)
print(f"{F}F Temp in Celcius: {C}")

# #### 5. Leap Year Identifier
# This function identifies if the provided year is leap year or not.

# A leap year is a year which has 366 days instead of 365.

# Logic - A year is a leap year if:

# - It is divisible by 4.
# - But if it's a century year (ends in 00 like 1900, 2100), it is not a leap year...
# - Unless it is also divisible by 400 (like 2000 or 2400).

#input year
year = 2028

#---------------------------------------------------------------------------------------
#defining function
def leap_year(y):
    """
    Identifies if the provided year is Leap Year or not.

    Input : Takes 1 positive integer value

    Return Boolean values: True if leap year, False if not leap year.
    """
    if y%4 == 0:             #if it is divisible by 4
        if y%100 == 0:       #if it is a century year
            if y%400 == 0:   #if its a century year but also divisble by 400
                return True
            else:
                return False    #divisible by 4 and 100, but not 400. Non-leap year
        else:
            return True         #divisible by 4 but not 100. Leap year
    else:
        return False            #not divisible by 4. Non-leap year

#-----------------------------------------------------------------------------------------------

#Calling the function
result = leap_year(year)

print(f"Is {year} Leap year: {result}")
