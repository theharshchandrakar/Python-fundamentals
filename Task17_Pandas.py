# ## Task 17: Pandas (Series and DataFrame)
# Pandas is the most popular Python library for data analysis and manipulation.

# #### 1. Pandas Series (1D Data)

# A Series is a one-dimensional array-like object. It can hold any data type (integers, strings, floats, etc.), and every single value has an index.

import pandas as pd

# Creating a Series with default numeric indexing (0, 1, 2...)
temperatures = pd.Series([32, 35, 28])

# Creating a Series with custom text labels as index strings
sales = pd.Series([100, 250, 400], index=["Mon", "Tue", "Wed"])

print(sales)

# #### 2. Pandas DataFrame (2D Data)

# A DataFrame is a two-dimensional, size-mutable, tabular data structure with rows and columns.
#  It is a collection of Series objects stacked side-by-side, sharing the same row index.

import pandas as pd

# Creating a DataFrame using a standard Python dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data)
print(df)

# ### Excercises

# #### 1. Creating and Customizing a Pandas Series

# This program creates a 1D Pandas Series with custom text labels as index indicators instead of default numbers.

import pandas as pd

# creating index labels and data list
months = ["Jan", "Feb", "Mar"]
revenue = [12000, 15000, 18000]

# initializing the series structure
monthly_sales = pd.Series(data=revenue, index=months)      #if we dont add index, it will by default assign 1,2,3..
print("--- Monthly Sales Series ---")
print(monthly_sales)                                       # displays the labeled 1D series data

# #### 2. Loading and Exploring an External CSV File

# This program will demonstrate how to read a dataset from a CSV file into a DataFrame and use structural commands to quickly preview and explore the data properties.

import pandas as pd

# target dataset location path
csv_file = "Task17_employee_data.csv"

#ingest and analyze the dataset file
try:
    df = pd.read_csv(csv_file)
    
    print("--- First 3 Rows ---\n")
    print(df.head(3))               # displays the top 3 preview rows of the dataset
    
    print("\n--- File Structure Information ---\n")
    df.info()                       # prints data types, column names, and missing values count
    
except FileNotFoundError as fnfe:
    print(f"The file {csv_file} could not be located!")        # displays message if file not found.

# #### 3. Filtering Data Based on Conditional Logic

# This program will slice rows out of a DataFrame by evaluating numeric values against a condition rule (where the item costs more than $100)

import pandas as pd

# 1. Prepare the raw data (a simple dictionary)
store_data = {
    "Item": ["Laptop", "Mouse", "Monitor", "Keyboard","Headphone"],
    "Price": [1200, 25, 300, 75,125]
}

# 2. Convert the dictionary into a spreadsheet table (DataFrame)
df = pd.DataFrame(store_data)

# 3. Filter: Keep only items where the Price is greater than 100
expensive_items = df[df["Price"] > 100]

# 4. Display the results
print("--- Items over $100 ---")
print(expensive_items)

# #### 4. Adding and Modifying Columns (Feature Creation)

# This program shows how to apply vector operations across existing DataFrame columns to calculate and assign a new data column.

import pandas as pd

# dataset containing item metrics
sales_logs = {
    "Product": ["Gadget A", "Gadget B", "Gadget C"],
    "Unit_Price": [3.5, 2.2, 5.1],
    "Units_Sold": [100, 40, 200]
}

df = pd.DataFrame(sales_logs)

# calculating total revenue per item by multiplying columns
df["Total_Revenue"] = df["Unit_Price"] * df["Units_Sold"]  # dynamically computes and appends new data column
print("--- Updated Sales Ledger ---")
print(df)                                                  # displays dataset containing the new field transformation

# #### 5. Exporting Aggregated Summary Data to Excel

# This program performs a simple calculation to check dataset metrics and write the final summary report table into an Excel spreadsheet file.

# NOTE- The program requires a dependency to export excel file, but if not found, it will install the dependency on the current environment.

import pandas as pd

# raw data
student_records = {
    "Class": ["Math", "Science", "Math", "Science", "Math"],
    "Score": [85, 90, 78, 92, 95]
}

#creating Dataframe
df = pd.DataFrame(student_records)

# calculating the average performance score per subject grouping
try:
    class_averages = df.groupby("Class").mean()
    
    # saving the resulting summarized table directly into an Excel sheet
    output_filename = "Task17_exported_sheet.xlsx"
    class_averages.to_excel(output_filename)
    
    print(f"Summary generated! Saved table successfully to '{output_filename}'")

except ModuleNotFoundError as mnfe:
    #printing module not found message, and installing it
    print(f"Missing dependency 'openpyxl', installing now")
    import subprocess
    subprocess.check_call(["pip", "install", "openpyxl"])
    
    class_averages.to_excel(output_filename)        #writing the file after the installation
    print(f"Installation complete! Saved table successfully to '{output_filename}'")
