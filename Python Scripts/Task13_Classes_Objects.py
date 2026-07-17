# ## Task 13: OOP- Classes and Objects
# In Python, Classes and Objects are the foundation of Object-Oriented Programming (OOP). They allow you to bundle data and functionality together.

# #### What is a Class?

# A class is a user-defined template or prototype. It defines the attributes (data) and methods (functions) that the objects created from it will have.

# #### What is an Object?

# An object is an instance of a class. When a class is defined, no memory is allocated until you create an object from it. You can create as many unique objects from a single class as you want.


# #### What is a Constructor?
# A constructor is a special method inside a class that Python calls automatically whenever you create a new object from that class.

# Its main job is to initialize (set up) the starting attributes of an object so it is ready to use right away, instead of you having to assign data manually line-by-line later.

# #### 1. Creating a Basic Class and Object

# This program will demonstrate how to define a blueprint for a student and create a unique student object with specific details.
# Python

# defining the class blueprint
class Student:
    """Represents a school student and their academic status.

    Attributes:
        name (str): The full name of the student.
        grade (str): The current letter grade assigned to the student (e.g., 'A', 'B').
    """

    #Constructor
    def __init__(self, name, grade):    #self points to the object being initialized in the runtime
        self.name = name                                       # stores the student's name attribute
        self.grade = grade                                     # stores the student's grade attribute

    def display_info(self):
        """Displays the information about the student, i.e Name, Grade"""
        print(f"Student Name: {self.name}, Grade: {self.grade}") # prints the student's complete information

# creating an instance object of the class
student1 = Student("Alice", "A")                                #Parameters are name and grade 

# accessing class functionality
student1.display_info()                                        # calls the method to view student1's details

# #### 2. Using Class Methods with Arguments

# This program will demonstrate how to add a behavior (a function) to a class that processes external data without needing a constructor.

# defining the class blueprint
class Calculator:
    """A class providing basic mathematical operations.
    
    This class handles functional math computations without maintaining any internal object state or attributes.
    """
    def add_numbers(self, num1, num2):
        """Performs addition on two numbers and prints the result to the console"""
        result = num1 + num2                                   # performs addition on the passed numbers
        print(f"The total sum is: {result}")                   # displays the final calculation result

# creating an instance object of the class
my_calc = Calculator()

# using the class functionality
my_calc.add_numbers(10, 20)                                    # passes 10 and 20 directly into the method

# #### 3. Using Class Methods to Modify Attributes

# This program will demonstrate how to build a class for a simple bank account and use a method to update the balance attribute dynamically.


# defining the class blueprint
class BankAccount:
    """A blueprint representing a financial bank account for a customer.

    Attributes:
        owner (str): The name of the person who owns the account.
        balance (int, float): The current amount of money available in the account.
    """
    def __init__(self, owner, balance):
        """Initializes a new BankAccount instance with an owner and a starting balance."""
        self.owner = owner                                     # stores the account owner's name
        self.balance = balance                                 # stores the current account balance

    def deposit(self, amount):
        """Adds a specified financial amount to the account balance.

        Arguments:
            amount (int, float): The quantity of money to be deposited.
        """
        self.balance += amount                                 # updates the balance attribute by adding money
        print(f"Deposited ${amount}. New Balance: ${self.balance}") # displays the transaction confirmation

# creating an instance object of the class
my_account = BankAccount("Bob", 500)

# performing transactions on the object
my_account.deposit(150)                                        # adds $150 to Bob's initial $500 balance
