# ## Task 16: Numpy (arrays, indexing, slicing, operations)

#We have to import numpy to start numpy operations
import numpy as np

#this cell must be run for other cells to execute.

# ### 1. NumPy Arrays (ndarray)

# A NumPy array is a grid of homogeneous (same data type) values.

#  Unlike Python lists, which can hold mixed types and are scattered in memory, NumPy arrays store data in one continuous block of memory. This allows for fast calculations.


# Creating a 1D array from a list
arr_1d = np.array([10, 20, 30, 40, 50])
print(f"1D array:\n {arr_1d}\n")

# Creating a 2D array (Matrix)
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]])

print(f"2D matrix:\n {matrix}")

# ### 2. Indexing

# Indexing is how you grab a specific single element from an array. It uses square brackets [] and is zero-indexed (starts at 0).

#     For 1D arrays: Use a single index value.

#     For 2D arrays: Use the format [row, column].

arr_1d = np.array([10, 20, 30, 40, 50])

# 1D Indexing
print("Accessing single element from 1D array")
print(arr_1d[0])           # Output: 10 (first element)
print(arr_1d[-1],"\n")     # Output: 50 (last element)

# 2D Indexing [row, column]
print("Accessing single element from 2D array")
print(matrix[0, 1])   # Output: 2 (row 0, column 1)
print(matrix[1, 2])   # Output: 6 (row 1, column 2)

# ### 3. Slicing

# Slicing allows you to extract a subarray or a chunk of data. The basic syntax is [start:stop:step], where stop is exclusive (not included).

arr_1d = np.array([10, 20, 30, 40, 50])

# Slicing a 1D array
print(f"Slicing 1D array: {arr_1d[1:4]}")     # Prints only the 1,2,3 index of array

# Slicing a 2D array [row_slice, column_slice]
# Grab all rows, but only the first two columns:
print(f"Slicing 2D array:\n {matrix[:, 0:2]}")

# ### 4. Vectorized Operations

# In pure Python, if you want to add 5 to every item in a list, you have to write a for loop. NumPy uses vectorization, which applies mathematical operations to the entire array instantly without loops.

# #### NumPy Broadcasting

# If you try to perform operations on arrays of different sizes, NumPy will automatically stretch or duplicate the smaller array to match the shape of the larger array behind the scenes. This is called broadcasting.

arr_1d = np.array([10, 20, 30, 40, 50])
print(f"Original arrray: {arr_1d}\n")

# Element-wise math
print(f"Addition of 5: {arr_1d + 5}")     # Output: [15, 25, 35, 45, 55]
print(f"Doubled element values: {arr_1d * 2}")     # Output: [20, 40, 60, 80, 100]

# Math between two arrays of the same shape
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"\nAdding values of array {a} and {b} = {a + b}")          # Output: [5, 7, 9]

# ### Excercises

# #### 1. Creating a Even Number Array

# This program shows how to create a 1D numpy array containing even numbers within a specific range using np.arange.



import numpy as np

# creating an array of even numbers from 2 to 10

even_array = np.arange(2, 11, 2)
print("Generated Array:", even_array)                      # displays the resulting 1D array


# #### 2. Accessing Elements in a 2D Array (Matrix Indexing)

# This program will demonstrate how to pinpoint and extract a single specific element from a 2D matrix using row and column indexing coordinates.

#Note - Index is 0 based, indexing starts from 0,1,2...
import numpy as np

# initializing a 2x3 matrix
matrix = np.array([[10, 20, 30], 
                   [40, 50, 60]])

# extracting the element
try:
    target_element = matrix[1, 1]   #accesses the element of 1st column of 1st row
    print(f"The element at row 1, col 1 is: {target_element}")  
    
except IndexError as ie:
    print("Requested row or column index is out of bounds!")    #if the provided elements is out of index range.


# ##### 3. Extracting a Chunk of Data (Matrix Slicing)

# This program shows how to slice a 2D array to extract all rows but only specific target columns.


import numpy as np

# initializing a 3x3 grid matrix
grid = np.array([[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]])

# slicing out the first two columns across all rows
try:
    column_slice = grid[:, 0:2]
    print("Sliced Sub-array:\n", column_slice)                  # displays the extracted vertical columns chunk
    
except Exception as e:
    print(f"An unexpected error occurred during slicing: {e}")


# ##### 4. Vectorized Scalar Operations

# This program will demonstrate how NumPy applies basic mathematical operations element-wise across an entire array without using any for loops.


import numpy as np

# initializing a base data array
data = np.array([1, 2, 3, 4, 5])

# multiplying every element in the array by 10 simultaneously
scaled_data = data * 10

# verifying the vector transformation
print("Original Data:", data)
print("Scaled Data (x10):", scaled_data)                        # displays the transformed array results


# ##### 5. Filtering Data with Boolean Masking

# This program will demonstrate how to filter out specific values inside an array based on a logical condition rule.


import numpy as np

# initializing an unsorted data array
scores = np.array([45, 88, 62, 95, 30])

# applying a logical condition to filter scores greater than 60
passing_scores = scores[scores > 60]
print("Scores above 60:", passing_scores)                   # extracts and displays only matching elements
