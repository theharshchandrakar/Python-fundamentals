# ## Task 15: OOP- Encapsulation and Abstraction

# ### - Encapsulation

# Encapsulation is the practice of bundling data (attributes) and methods together inside a class, while restricting direct access to some of the object's components.

# It prevents outside code from accidentally tampering with or changing internal data.

# Python restricts access by adding double underscores '__' before an attribute name to make it private. You then use special public methods called Getters and Setters to safely view or modify that data.

#     Getter: A method used to read the value of a private attribute safely.

#     Setter: A method used to modify the value of a private attribute safely, including validation checks.

# defining the class
class SmartPhone:
    # double underscores make this a private attribute
    __battery_life = 100                                   # safely hidden from direct outside access

    def get_battery(self):
        return self.__battery_life                         # getter: safely reads and returns the private data

    def use_phone(self, battery_used):
        if battery_used > 0 and self.__battery_life >= battery_used:
            self.__battery_life -= battery_used            # setter method
            print(f"Phone used. Remaining battery: {self.__battery_life}%")
        else:
            print("Invalid usage or not enough battery!")  # displays validation error alternative message

# creating an instance object of the class
my_phone = SmartPhone()

# accessing the private attribute via public methods
my_phone.use_phone(85)                                  # utilizes setter logic to reduce battery level
print(f"Current charge: {my_phone.get_battery()}%")     # utilizes getter logic to check current battery status

# ### - Abstraction

# Abstraction means hiding the complex internal details of how something works and only showing the essential features needed to use it.

# It reduces complexity by hiding the "how" and focusing entirely on the "what".

# In Python, abstraction is achieved using the abc (Abstract Base Classes) module. You create a template class that declares a method must exist, but leaves it empty so child classes can figure out their own complex implementation.

# You cant make an instance of an abstract class

#importing ABC
from abc import ABC, abstractmethod

# defining the abstract base class template
class VehicleTemplate(ABC):
    @abstractmethod
    def press_start_button(self):
        pass                                          # abstract method: defines the rule but leaves it empty

# defining the concrete child class that implements the hidden details
class SportsCar(VehicleTemplate):
    def press_start_button(self):
        print("Start button is pressed...")
        print("Sending electrical signal to starter motor...") # step 1 of complex internal machinery
        print("Injecting fuel into the cylinders...")          # step 2 of complex internal machinery
        print("Spark plugs ignited. Engine is roaring!")       # step 3 of complex internal machinery

# creating an instance object of the concrete car class
my_car = SportsCar()

# interacting with the simple abstract interface
my_car.press_start_button()
