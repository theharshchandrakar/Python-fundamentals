# ## Task 5: 5 Loop-based Excercises

# ### Loops
# Loops allow you to execute a block of code repeatedly.

# Python has two primary types of loops:
# - for loops
# - while loops.

# ### 1. for Loops
# Used when you want to iterate over a sequence (like a list, string, or a range of numbers) a specific number of times.

# ##### 1. Printing Numbers
# We will print numbers from 0 to n using for loop

#input (upper limit)
n = 5

'''range() function is used to iterate over the values provided as start, end number with an optional parameter to skip numbers in each iteration'''
for num in range(0,n):
    print(num)

#note that range function excludes the upper limit

# ##### 2. List Iteration
# We can iterate through any iterable and with any data type.

#input list
colors = ['red','orange','green','blue','pink']

'''This loop will iterate through all the elements in the color list and print them out'''
for color in colors:
    print(color)

# ### 2. while Loop

# Used when you want to repeat a block of code as long as a specific condition remains True.

# If the condition never turns false, it might go on Infinite Loop.

# [Press Ctrl+C to force kill a running instance]

# ##### 3. Countdown
# Countdown always stops when it reaches 0

#This input variable tells from where to start the countdown from
n = 3

'''We use the logic of code being executed until the value of n reaches 0'''
while n!=0:
    print(n)
    n -= 1          #updates the value of n, so that it doesnt loop infinitely.
else:
    print('Countdown Finish') #this code executes when the condition is not met, i.e n = 0

# ##### 4. Input Loop
# We can add other functions in the loop, so they keep repeating until the required condition is met.

#input() function allows to take input from the user
# number = int(input("Please enter an even number: "))
number = 4  # Default value for testing


'''This code will keep asking for input until the user inputs an even number'''
while number==0 or number%2 != 0:
    # number = int(input("Incorrect! Please enter an even number: "))
    number = 4  # Default value for testing
else:
    print('Thank you!') #this code executes when the user enters an even number.S

# ### 3. Loop Control Statements

# These keywords alter the flow of your loops:

#     break: Exits the loop entirely.

#     continue: Skips the rest of the current iteration and jumps to the next one.

# ##### 5. ATM Setup
# This program is an ATM setup with withdrawl requests. It processes the requests and give results accordingly.

# We use break and continue for certain conditions.

# Initial ATM setup

'''requests are the amount withdrawl requests asked by the user. you can change values to test outputs'''
requests = [200, 500, -100, 1200, 300, 2500, 100, 200]
'''This is the total amount in the bank account'''
atm_funds = 2000
request_no = 0          #this will identify the request no in the output.


#for loop to iterate over all the requests provided.
for amount in requests:
    request_no+=1
    print(f"Request no: {request_no}, Request amount: {amount}")
    
    # 1. Skip invalid amounts.
    if amount <= 0:
        print(f"Invalid Input. Try Again!\n")
        continue        #skips the further process and starts a new iteration
        
    # 2. Skip if request amount is greater than total remaining funds.
    if amount > atm_funds:
        print(f"Insufficient ATM funds!.\n")
        continue        #skips the further process and starts a new iteration
        
    # 3. Process successful withdrawal
    atm_funds -= amount
    print(f"Dispensed: ${amount}. Remaining ATM funds: ${atm_funds}\n")
    
    # 4. Break immediately if ATM becomes completely empty
    if atm_funds == 0:
        print("ATM is out of cash. Shutting down.")
        break           #stops the loop and proceed to further program (if any)

# Notice that we didnt process Request no. 8 because Request no 7 met the condition with 'break' statement.
# So the loop exited early.
