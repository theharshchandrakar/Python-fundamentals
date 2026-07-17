# ## Task 6: 5 list Excercise

# #### List:
#  A list is a mutable, ordered collection of items enclosed in square brackets [] that allows you to add, remove, or modify elements after it is created.

# #### List Methods

# Lists are mutable, so their methods directly modify the original list by adding, removing, or rearranging elements.

#     .append(item): Adds an item to the very end of the list.

#     .insert(index, item): Inserts an item at a specific position/index.

#     .remove(item): Removes the first occurrence of a specific value.

#     .pop(index): Removes and returns the item at the given index (defaults to the last item).

#     .sort(): Sorts the items in ascending order in-place.

# ##### 1.Adding Elements

#This is our original list containing names of cities
cities = ["London","Paris"] 
print(f"Original list: {cities}\n")


#add one element to the end of the list - append method
cities.append("Raipur")
print(f"List after adding one city: {cities}\n") 


#add element on a particular index in list - insert method
cities.insert(2,"Pune")
print(f"List after adding city between elements: {cities}\n")


#add other list (or iterable) to the list - extend method
more_cities = ["Indore","Guwahati","Goa"]   #list of some more cities to be added
cities.extend(more_cities)
print(f"List after adding elements from other list: {cities}")

# ##### 2. Sorting
# Sorts the list in ascending/descending order

#original list
Names = ["Andy","Pope","Clare","Yote","Johan"]
Numbers = [2,6,35,8,1,0,-3]
print(f'''Original list: {Names}
Number List:{Numbers}\n''')


#sorting
#Ascending
Names.sort()
Numbers.sort()
print(f'''Sorted list: {Names}
Sorted Numbers: {Numbers}\n''')


#Descending
#reverse sorts the elements in descending order
Names.sort(reverse=True)
Numbers.sort(reverse=True)        
print(f'''Descending Sorted list: {Names}
Descending Sorted Numbers: {Numbers}''')

# ##### 3. Remove Elements

#Original list
og_list = ["Harsh",5,13,True,3.14,False]
print(f"Original List: {og_list}\n")


# remove first element with specified value - remove
og_list.remove(True)
print(f"List after removing True: {og_list}\n")


# remove element on specified position - pop
og_list.pop(3)          #remove element on 3rd index
print(f"List after removing 3rd index element: {og_list}\n")


# remove all elements from list - clear
og_list.clear()          
print(f"List after removing all elements: {og_list}\n")

# ##### 4. Length and Count

#original list
oglist = [3,1,4,6,6,2,13,54,5,5,5,5]
print(f"Original list: {oglist}\n")


#Calculate length of list (No of elements)
print(f"No of elements in list: {len(oglist)}\n")


#Count the occurence of an element
value = 5       #element to be counted
print(f"No of elements of value {value}: {oglist.count(value)}")

# #### Tuple:
#  A tuple is an immutable, ordered collection of items enclosed in parentheses () that cannot be changed, appended, or altered once it is defined.

# #### Tuple Methods

# Tuples are immutable (unchangeable), so they have very few methods. They only have methods to inspect their contents, never to modify them.

#     .count(item): Returns the total number of times a specific value appears in the tuple.

#     .index(item): Returns the position (index) of the first occurrence of a specific value.

# ##### 5.Count and Index method

#original tuple
oglist = ("A","E","D","A","C","A")
print(f"Original tuple: {oglist}\n")


#Find index of first occurence of specified element 
value = 'C'
print(f"Index of {value}: {oglist.index(value)}\n")


#Count the occurence of an element
value = "A"     #element to be counted
print(f"No of elements of value {value}: {oglist.count(value)}")
