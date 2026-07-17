# ## Task 4: 3 IF/Else Excercises

# ### if-else Statements
# if: Executes code if the condition is true.

# elif (else if): Checks another condition if the previous ones were false.

# else: Executes code if all previous conditions were false.

# ### 1. ODD/EVEN program

#Input
number = 58

'''We use the logic of when a number is divided by 2, if it leaves 0 remainder it is EVEN
But when the remainder is 1, it is ODD'''
if number%2 == 0:
    print(f"Number {number} is EVEN")
else:
    print(f"Number {number} is ODD")

#Input
number = 59

'''We use the same logic for an ODD input'''
if number%2 == 0:
    print(f"Number {number} is EVEN")
else:
    print(f"Number {number} is ODD")

# ## 2. Age Category

#input age
'''try changing age value to see different outcomes'''
age = 19

'''We use 'elif' to add multiple conditions in our statement.'''
if age<12:
    print("Child")
elif age>12 and age<20:
    print("Teenager")
else:
    print("Adult")

# ## 3. Pass-Fail Check

'''we can use multiple variables in our condition to make our program dynamic'''

#inputs
passing_mark = 50
score = 20

#Note: elif and else statements are optional.
if score>=passing_mark:
    print("Passed")
elif score<passing_mark:
    print("Failed")
