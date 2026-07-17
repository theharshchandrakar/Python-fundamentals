# ## Task 7: Sets and Dictionaries

# ### SET
# A set is an unordered, mutable collection of unique elements enclosed in curly braces {} that automatically filters out duplicate values and does not support indexing.

# ###### Note - Once a set is created, you cannot modify the elements, but can add or remove elements.

# ##### 1. Common Set Methods

#     .add(item): Adds a single element to the set (if it's not already present).

#     .remove(item): Removes a specific element; raises a KeyError if the element doesn't exist.

#     .discard(item): Removes a specific element, but will not crash your code if the item isn't found.

#     .clear(): Removes all elements, leaving an empty set.

#set with some initial fruits (duplicates are automatically removed)
fruits = {"apple", "banana", "cherry", "apple"}
print(f"Initial set (duplicates removed): {fruits}\n")

# .add() : Adds a single element to the set
fruits.add("orange")
print(f"After adding orange: {fruits}\n")

# .discard() : Removes an element safely (won't crash if it doesn't exist)
fruits.discard("cherry")
print(f"After removing cherry: {fruits}\n")

# .remove() : Also removes an element, but would crash if the element wasn't there
fruits.remove("apple")
print(f"After removing apple: {fruits}\n")

# .clear() : Empties the entire set
fruits.clear()
print(f"After clearing set (Empty set): {fruits}")

# ##### 2. Mathematical Operations
# Sets excel at finding relationships between different collections of data using standard Venn diagram math:

#     Union (| or .union()): Combines all unique elements from both sets.

#     Intersection (& or .intersection()): Finds only the elements present in both sets.

#     Difference (- or .difference()): Returns elements in the first set that are not in the second set.

#We create 2 sets to perform opertations on
group_a = {1, 2, 3}
group_b = {3, 4, 5}
print(f'''Original sets:
{group_a}
{group_b}\n''')

#Performing operations and printing the result
print(f"Unions of both sets: {group_a | group_b}\n")  # Union: {1, 2, 3, 4, 5}
print(f"Intersection of both sets: {group_a & group_b}\n")  # Intersection: {3}
print(f"Differences of both sets: {group_a - group_b}\n")  # Difference: {1, 2}

# ### DICTIONARY

# Dictionaries are written with curly brackets and are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# ###### Note - As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# ##### 3. Dictionary Operations

# Creating a dictionary {key:value}
user = {"name": "Alice", "age": 25, "city": "New York"}
print(f"Original Dictionary: {user}\n")


# Accessing a value using its key
print(f"Accessing value using key 'name': {user["name"]}\n")  # Output: Alice

# Adding a key-value pair
user["email"] = "alice@email.com"
print(f"Adding new element 'email': {user}\n")  # Adds a new pair

#Updating a key-value pair
user["age"] = 28                   # Updates existing key
print(f"Updating 'age' to 28: {user}")

# ##### 4.Retrieval Methods
#     .get(key, default): Safely fetches a value. If the key doesn't exist, it returns None (or a custom default value) instead of throwing a KeyError crash.

#     .keys(): Returns a view object containing all the keys in the dictionary.

#     .values(): Returns a view object containing all the values.

#     .items(): Returns a view object containing tuples of (key, value) pairs, perfect for looping.

#Dictionary with student information
student = {"name": "John", "grade": "A", "age": 18}
print(f"Initial dictionary: {student}\n")


# .get() : Doesnt throw error when value is not found
print(f"City (using get): {student.get('city', 'Not Found')}\n")


# .keys()
print(f"Keys: {list(student.keys())}")
# .values()
print(f"Values: {list(student.values())}")
# .items() 
print(f"Items: {list(student.items())}\n")

# ##### 5. Modification and Removal Methods

#     .update(other dict): Merges another dictionary or iterable of pairs into the current one, overwriting existing keys.

#     .pop(key): Removes the specified key and returns its associated value.

#     .popitem(): Removes and returns the last inserted (key, value) pair as a tuple.

#     .clear(): Empties the entire dictionary.

#Dictionary with student information
student = {"name": "John", "grade": "A", "age": 18}
print(f"Initial dictionary: {student}\n")


# .update() - Modify and Add multiple key-value pairs
student.update({"grade": "A+", "major": "CS"})
print(f"After adding multiple key-values: {student}\n")


# .pop() : Remove a specific key
removed_age = student.pop("age")
print(f"Removed age: {removed_age}")
print(f"Dictionary after Removal: {student}")
