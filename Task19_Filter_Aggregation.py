# ## Task 19: Filter, Aggregation and GroupBy

#NOTE - This is the dataframe creation cell. This cell execution is crucial for all the below cells to work

import pandas as pd

# Creating a clean dataset containing data 
data = {
    "Student": ["Alice", "Bob", "Charlie", "Diana", "Evan", "Fiona"],
    "Class": ["Math", "Science", "Math", "Science", "Math", "Science"],
    "Score": [85, 92, 78, 95, 90, 88]
}

# Converting into a DataFrame
df = pd.DataFrame(data)

# Displaying the raw DataFrame to verify it loaded correctly
print(df)

# #### 1. Filtering (Extracting Specific Rows)

# Filtering is the process of scanning a dataset and selecting only the rows that meet a specific logical condition (like a custom search filter).

# Select only rows where the score is greater than 80
high_scores = df[df["Score"] > 80]
print(high_scores)

# #### 2. GroupBy (Splitting the Data into Buckets)

# groupby() splits the dataset into separate, hidden buckets based on a category. By itself, grouping doesn't give a result, it just organizes the data behind the scenes so we can perform calculations on each bucket individually.

# Group the dataset by the "Class" column (creates a Math bucket, Science bucket, etc.)
grouped_data = df.groupby("Class")
print(grouped_data)

#It doesnt give out any output, thats why when we print it shows groupby object and location

# #### 3. Aggregation

# Aggregation takes a collection of many values and merges them down into a single mathematical summary metric (like a total sum, an average, or a count).

#  Common functions include .mean(), .sum(), .count(), .max(), and .min().

# Calculate the average of a specific column
average_score = df["Score"].mean()
print(average_score)

# ##### 1: Finding the Highest Score
# Goal: Find the absolute highest score achieved by any student in the dataset.

# .max() - returns the highest value across a specified axis in a DataFrame or Series
highest_score = df["Score"].max()

#printing result
print(f"Highest Score: {highest_score}")

# ##### 2: Counting Total Students

# Goal: Find out how many total student records/entries are in the dataset.

# .count() is used to count the number of non-null values across a specific axis of a DataFrame

total_students = df["Student"].count()

print(f"Total Students: {total_students}")

# ##### 3: Filtering Passing Students

# Goal: Extract a list of students who scored a passing grade of 80 or higher.


# We filter the scores to include only students who meets the condition
passing_students = df[df["Score"] >= 90]

print(f"Passing Students: {passing_students}")

# ##### 4: Grouped Counting (Students Per Class)

# Goal: Find out how many students are enrolled in each specific class type.

# We filter students by Class and group them by .count():

students_per_class = df.groupby("Class")["Student"].count()

print(f"Students per Class:{students_per_class}")

# ##### 5: Grouped Maximums and Minimums (Highest and Lowest Score per Class)

# Goal: Find out what the highest and lowest single score achieved was in each separate subject grouping.



# We use grouping first, then use aggregation on the grouped data 
highest_per_class = df.groupby("Class")["Score"].max()
print(f"Highest Score per Class: {highest_per_class}\n")

# Same logic for .min() aggregation
lowest_per_class = df.groupby("Class")["Score"].min()
print(f"Lowest Score per Class:{lowest_per_class}")
