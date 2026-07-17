# ## Task 20: Date & Time Manipulation & Mini Project

# In data analysis, date and time information often arrives as messy, non-standardized text strings. This task focuses on utilizing the `datetime` module and Pandas tools to parse these strings into actual date objects.

# ### Core Concepts
# - pd.to_datetime(): This function converts text strings into proper Python datetime objects so Pandas can understand them as actual dates rather than plain words.

# - The .dt Accessor: Once a column is officially a date type, you can use .dt.month or .dt.year to instantly extract the month or year.


# ##### Example
# - Convert text to actual date format:

#     df["Date"] = pd.to_datetime(df["Raw_Date_String"])


# - Extract parts of the date into brand new columns:


#     df["Year"] = df["Date"].dt.year
#     df["Month"] = df["Date"].dt.month

# ### Mini Project: Data Cleaning & Temporal Analysis

# This mini-project demonstrates a complete end-to-end data pipeline using a raw retail sales dataset.

# **Objectives:**
# 1. **Data Cleaning:** Handle missing transaction revenue records using imputation techniques.
# 2. **Datetime Parsing:** Convert flat text timestamps into structural datetime objects.
# 3. **Feature Engineering:** Extract distinct monthly and yearly tracking attributes from the standardized dates.
# 4. **Aggregated Insights:** Apply group-by summaries to analyze macro financial performance and track revenue trends over time.

# #### Step 1. SETUP: Loading the Large Dataset
# Importing the 150-row messy CSV file into a DataFrame

import pandas as pd

#we import data from csv file and convert into dataframe 
df = pd.read_csv("Task20_RawData.csv")

print("First 5 Rows")

#since the dataset is large, we use .head() to display first few lines of the data
print(df.head())

# #### Step 2. DATA CLEANING
# Handle missing data by filling blank or null values in revenue column with 0

df["Revenue"] = df["Revenue"].fillna(0)

#result
print(df.head())

# #### 3. DATE & TIME MANIPULATION

#  Convert the messy text column into a standardized datetime format

#  format='mixed' allows Pandas to handle multiple string patterns.


df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"], format='mixed')

# Extract the Month and Year into separate new columns
df["Year"] = df["Purchase_Date"].dt.year
df["Month"] = df["Purchase_Date"].dt.month

print(f"Data After Date Extraction & Cleaning: \n{df.head()}")

# #### 4. ANALYSIS: GroupBy & Aggregation
# Calculate the total revenue generated per year

#We group by year and sum the values in Revenue column
yearly_revenue = df.groupby("Year")["Revenue"].sum()

# Calculating the total revenue per product 
product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)


#.to_string() is a function that converts a DataFrame into a single, clean plain-text string.
print("Final Aggregated Analysis: Revenue Per Year:")
print(yearly_revenue.to_string())

print("\n Final Aggregated Analysis: Top Products by Revenue")
print(product_revenue.to_string())
