'''
What is Pandas?
Pandas is a Python library used for working with data sets.

It has functions for analyzing, cleaning, exploring, and manipulating data.

The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis"

Why Use Pandas?
Pandas allows us to analyze big data and make conclusions based on statistical theories.

Pandas can clean messy data sets, and make them readable and relevant.

Relevant data is very important in data science.

Data Science: is a branch of computer science where we study how to store, use and analyze
data for deriving information from it.

What Can Pandas Do?
Pandas gives you answers about the data. Like:
Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?
Pandas are also able to delete rows that are not relevant, or contains wrong values,
like empty or NULL values. This is called cleaning the data.
'''

# Import necessary libraries
import numpy as np
import pandas as pd

# --------------------------------
# 1. BASIC PYTHON + NUMPY EXAMPLE
# --------------------------------
data = np.array([10, 20, 30, 40])
print("NumPy Array:", data)
print("Mean:", np.mean(data))
print()  # Blank line for readability

# OUTPUT:
# NumPy Array: [10 20 30 40]
# Mean: 25.0


# ================================
# 2. PANDAS SERIES
# ================================
print("=== PANDAS SERIES ===")

# Create a Series from a list
s = pd.Series([10, 20, 30, 40])
print("Series:\n", s)

# OUTPUT:
# 0    10
# 1    20
# 2    30
# 3    40

# Series with custom index
s2 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
print("\nSeries with Custom Index:\n", s2)

# Accessing elements
print("\nAccess by label s2['b']:", s2['b'])        # 200
print("Access by position s2[1]:", s2[1])          # 200
print()


# ================================
# 3. PANDAS DATAFRAME
# ================================
print("=== PANDAS DATAFRAME ===")

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# OUTPUT:
#       Name  Age       City
# 0    Alice   25      Delhi
# 1      Bob   30     Mumbai
# 2  Charlie   35  Bangalore


# --------------------------------
# Accessing columns
# --------------------------------
print("\nColumn - Name:\n", df['Name'])

# Accessing rows
print("\nRow using loc (index=1):\n", df.loc[1])
print("\nRow using iloc (3rd row):\n", df.iloc[2])


# --------------------------------
# Adding new column
# --------------------------------
df['Salary'] = [50000, 60000, 70000]
print("\nDataFrame after adding Salary:\n", df)

# Filtering rows
adults = df[df['Age'] > 28]
print("\nRows where Age > 28:\n", adults)

# OUTPUT:
#          Name  Age       City  Salary
# 1         Bob   30     Mumbai   60000
# 2     Charlie   35  Bangalore   70000


# --------------------------------
# Summary statistics
# --------------------------------
print("\nSummary Statistics:\n", df.describe())

# OUTPUT:
#              Age        Salary
# count   3.000000      3.000000
# mean   30.000000  60000.000000
# min    25.000000  50000.000000
# max    35.000000  70000.000000


# --------------------------------
# Selecting multiple columns
# --------------------------------
print("\nSelecting Age and Salary columns:\n", df[['Age', 'Salary']])

# --------------------------------
# Slicing rows
# --------------------------------
print("\nSlicing first two rows:\n", df[0:2])
