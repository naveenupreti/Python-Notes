# ============================================================
#      PANDAS PROGRAM (data cleaning, anaylsing, sorting, merging)
# ============================================================

import numpy as np
import pandas as pd


# ------------------------------------------------------------
# 1. BASIC NUMPY EXAMPLE
# ------------------------------------------------------------
data = np.array([5, 10, 15, 20])
print("NumPy Array:", data)
print("Mean:", np.mean(data))
print()

# OUTPUT:
# NumPy Array: [ 5 10 15 20]
# Mean: 12.5


# ============================================================
# 2. PANDAS SERIES
# ============================================================
print("=== PANDAS SERIES ===")

s = pd.Series([100, 200, 300])
print("Series:\n", s)

# OUTPUT:
# 0    100
# 1    200
# 2    300
# dtype: int64

print()


# ============================================================
# 3. DATAFRAME CREATION
# ============================================================
print("=== ORIGINAL DATAFRAME ===")

data = {
    'Name': ['Amit', 'Bob', 'Cathy', 'Bob', None],
    'Age': [25, 30, None, 30, 40],
    'City': ['Delhi', 'Mumbai', 'Delhi', None, 'Chennai'],
    'Salary': [50000, 60000, 55000, None, 65000]
}

df = pd.DataFrame(data)
print(df)

# OUTPUT:
#    Name   Age     City   Salary
# 0   Amit  25.0    Delhi  50000.0
# 1    Bob  30.0   Mumbai  60000.0
# 2  Cathy   NaN    Delhi  55000.0
# 3    Bob  30.0      NaN      NaN
# 4   None  40.0  Chennai  65000.0


# ============================================================
# 4. DATA CLEANING
# ============================================================

print("\n=== REMOVE DUPLICATES ===")
df_clean = df.drop_duplicates()
print(df_clean)

# OUTPUT:
#    Name   Age     City   Salary
# 0   Amit  25.0    Delhi  50000.0
# 1    Bob  30.0   Mumbai  60000.0
# 2  Cathy   NaN    Delhi  55000.0
# 3    Bob  30.0      NaN      NaN
# 4   None  40.0  Chennai  65000.0


print("\n=== FILL MISSING VALUES ===")
df_filled = df_clean.fillna({
    "Name": "Unknown",
    "Age": df_clean["Age"].mean(),      # (25 + 30 + 30 + 40) / 4 = 31.25
    "City": "Not Specified",
    "Salary": df_clean["Salary"].median()  # (50000 + 55000 + 60000 + 65000)/4 = 57500
})
print(df_filled)

# OUTPUT (verified):
#       Name    Age           City   Salary
# 0     Amit  25.00          Delhi  50000.0
# 1      Bob  30.00         Mumbai  60000.0
# 2    Cathy  31.25          Delhi  55000.0
# 3      Bob  30.00  Not Specified  57500.0
# 4  Unknown  40.00        Chennai  65000.0


# ============================================================
# 5. SORTING
# ============================================================

print("\n=== SORT BY SALARY (Ascending) ===")
sorted_df = df_filled.sort_values("Salary")
print(sorted_df)

# OUTPUT:
#       Name    Age           City   Salary
# 0     Amit  25.00          Delhi  50000.0
# 2    Cathy  31.25          Delhi  55000.0
# 3      Bob  30.00  Not Specified  57500.0
# 1      Bob  30.00         Mumbai  60000.0
# 4  Unknown  40.00        Chennai  65000.0


print("\n=== SORT BY AGE (Descending) ===")
sorted_age = df_filled.sort_values("Age", ascending=False)
print(sorted_age)

# OUTPUT:
#       Name    Age           City   Salary
# 4  Unknown  40.00        Chennai  65000.0
# 2    Cathy  31.25          Delhi  55000.0
# 1      Bob  30.00         Mumbai  60000.0
# 3      Bob  30.00  Not Specified  57500.0
# 0     Amit  25.00          Delhi  50000.0


# ============================================================
# 6. GROUPING & AGGREGATION
# ============================================================

print("\n=== AVERAGE SALARY BY CITY ===")
grouped = df_filled.groupby("City")["Salary"].mean()
print(grouped)

# OUTPUT:
# City
# Chennai          65000.0
# Delhi            52500.0
# Mumbai           60000.0
# Not Specified    57500.0
# Name: Salary, dtype: float64


# ============================================================
# 7. MERGING TWO DATAFRAMES
# ============================================================

print("\n=== MERGING DATAFRAMES ===")

# Department table
dept_data = {
    'Name': ['Amit', 'Bob', 'Cathy', 'Unknown'],
    'Department': ['Sales', 'HR', 'IT', 'Admin']
}

dept_df = pd.DataFrame(dept_data)

merged = pd.merge(df_filled, dept_df, on="Name", how="left")
print(merged)

# OUTPUT:
#       Name    Age           City   Salary Department
# 0     Amit  25.00          Delhi  50000.0      Sales
# 1      Bob  30.00         Mumbai  60000.0         HR
# 2    Cathy  31.25          Delhi  55000.0         IT
# 3      Bob  30.00  Not Specified  57500.0         HR
# 4  Unknown  40.00        Chennai  65000.0      Admin
