# ## Task 14: Inheritance and Polymorphism


# ### - Inheritance

# Inheritance allows a new class (Child Class) to automatically adopt all the attributes and methods of an existing class (Parent Class). This prevents from writing duplicate code.

# #### 1. Animal behaviour
# This program demonstrates how inhertance works using an example of Animal class whose sub-class is Dog.

# Parent Class
class Animal:
    def walk(self):
        print("The animal can walk.")

# Child Class inherits from Animal by putting it in parentheses ()
class Dog(Animal):
    def bark(self):
        print("The DOG can bark.")

# Creating a dog object
my_dog = Dog()

#calling the function
'''This function is not present in Dog Class but since its inhertied from Animal class where this function is defined, it will execute'''
my_dog.walk()   # Inherited from Parent Class


'''This function is present in Dog Class therefore it will unconditionally execute.'''
my_dog.bark()  # Defined inside Child Class

# #### 2. Corporate Hierarchy and Bonus Tracking

# This program will demonstrate how a child class (Manager) can inherit base profile data from a parent class (Employee) and apply a logical function to process a role-specific bonus.
# Python


# defining the parent class
class Employee:
    """A parent class representing a generic company employee.

    Attributes:
        base_salary (int): The baseline salary shared across all entry-level positions.
    """
    base_salary = 50000                                         # a shared attribute for all employees

# defining the child class that inherits from Employee
class Manager(Employee):
    def calculate_total_pay(self, bonus_amount):
        """Calculates and displays the manager's final pay by combining base salary and bonus.

        Args:
            bonus_amount (int, float): The specific performance bonus for the manager.
        """
        total_pay = self.base_salary + bonus_amount             # accesses the inherited base_salary to add a unique bonus
        print(f"Total Manager payout is: ${total_pay}")         # displays the final payout

# creating an instance object of the child class
dept_head = Manager()

# calculating payroll data for the manager
dept_head.calculate_total_pay(15000)                            # runs the calculation using the inherited parent salary

# ### - Polymorphism

# Polymorphism allows different classes to have methods with the exact same name but different underlying behaviors.

# #### 3. Animal Sounds
# This program shows how different object use the same function but generate different output, just like real animals make sound but their sound is different per animal.

#creating 2 classes having the same function name

class Cat:
    def make_sound(self):
        print("Meow!")

class Cow:
    def make_sound(self):
        print("Moo!")


# Creating unique objects
obj_cat = Cat()
obj_cow = Cow()

# Notice they have the same function name but both trigger functions of different classes
obj_cat.make_sound()
obj_cow.make_sound()
