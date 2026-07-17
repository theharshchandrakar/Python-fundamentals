# ## Task 18: Data Cleaning
# Data Cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. Since real-world data is very messy, this is often where data scientists spend most of their time.

# In Python, Pandas is the ultimate tool for this job.

import pandas as pd

# 1. Importing the messy CSV file into a DataFrame
df = pd.read_csv("Task18_RawData.csv")

print("--- 1. Raw Dataset Before Cleaning ---")
print(df.head())
print("\n" + "="*50 + "\n")

#Running this cell is crucial for the below cells since the DataFrame is defined here, else they will throw error.

#Run this cell again if you want to create raw unclean DataFrame again.

# #### 1. Renaming Columns & Dropping Irrelevant Data

# The very first thing you should do after loading data is clean up the column names and remove irrelevant columns so that it is easier to read and dont waste time and resources on cleaning irrelevant column.


# Rename columns to fix typos or casing
df = df.rename(columns={"stu_scr": "Score", "CLS": "Class"})

# Drop completely unnecessary columns
df = df.drop(columns=["Unnecessary_Column_Name"])


#print result
print(f"Dataframe after Renaming Columns and Dropping Irrelevant Data: \n {df.head()}")

# #### 2. Handling Missing Data (NaN)

# Real datasets often have blank spots. We have two main choices: drop them entirely or fill them in with a placeholder.

# Drop any row that contains a missing value
df_clean = df.dropna()

# Alternatively, fill missing values with a 0 (or the column mean)
df["Score"] = df["Score"].fillna(0)

#print result
print(f"Dataframe after Handling missing data: \n {df.head()}")

# #### 3. Removing Duplicates

# Identical rows can slip into data collections due to system glitches or double-saving.


# Check how many duplicate rows exist
print(df.duplicated().sum())

# Remove duplicate rows, keeping only the first occurrence
df = df.drop_duplicates()


#print result
print(f"Dataframe after removing Duplicate data: \n {df.head()}")

# #### 4. Fixing Data Types

# Sometimes numeric data accidentally gets imported as text (strings), which breaks your math calculations.
# We have to convert them into valid data types



# Convert a column from text/object string to a proper integer
df["Age"] = df["Age"].astype(int)


#print result
print(f"Dataframe after fixing Data Types: \n {df.head()}")

# #### 5. Standardizing Text

# Text data entered by humans is often messy with inconsistent capitalization and invisible spaces.

# We need to standardize strings so the computer recognizes them as the same category.

# Standardize Text: Strip invisible spaces on the edges, and make everything Title Case
df["Class"] = df["Class"].str.strip().str.title()


# print result
print(f"Dataframe after Standardizing Text: \n {df.head(10)}")

# ### Showing Cleaned Data Result

print(f"Cleaned data:\n {df}")
