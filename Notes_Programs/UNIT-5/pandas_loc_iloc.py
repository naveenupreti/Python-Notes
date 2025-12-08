# ------------------------------------------------------------
# PROGRAM: Extracting Rows, Columns, Cells using loc/iloc
# ------------------------------------------------------------

import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 28],
    "City": ["Delhi", "Mumbai", "Chennai", "Pune"]
})

print("Original DataFrame:\n", df)

# OUTPUT:
#       Name   Age     City
# 0    Alice   25     Delhi
# 1      Bob   30    Mumbai
# 2  Charlie   35   Chennai
# 3    David   28      Pune
print("-" * 60)


# ============================================================
# 1. EXTRACTING ONLY ROWS
# ============================================================
print("\n1. Extracting ONLY ROWS")
print("---------------------------")

# loc (row labels)
print("\nUsing loc - Row with label 2:")
print(df.loc[2])

# OUTPUT:
# Name     Charlie
# Age      35
# City     Chennai

# iloc (row positions)
print("\nUsing iloc - Row at position 2:")
print(df.iloc[2])

# OUTPUT:
# Name     Charlie
# Age      35
# City     Chennai

# Multiple rows (loc includes end index)
print("\nUsing loc - Rows 1 to 3:")
print(df.loc[1:3])

# OUTPUT:
#       Name   Age     City
# 1      Bob   30    Mumbai
# 2  Charlie   35   Chennai
# 3    David   28      Pune

# Multiple rows (iloc excludes end index)
print("\nUsing iloc - Rows 1 to 3 (end excluded):")
print(df.iloc[1:3])

# OUTPUT:
#       Name   Age     City
# 1      Bob   30    Mumbai
# 2  Charlie   35   Chennai
print("-" * 60)


# ============================================================
# 2. EXTRACTING ONLY COLUMNS
# ============================================================
print("\n2. Extracting ONLY COLUMNS")
print("-----------------------------")

# loc column extraction
print("\nUsing loc - Column 'Name':")
print(df.loc[:, "Name"])

# OUTPUT:
# 0      Alice
# 1        Bob
# 2    Charlie
# 3      David

# iloc column extraction (column index 0)
print("\nUsing iloc - Column at position 0:")
print(df.iloc[:, 0])

# OUTPUT:
# 0      Alice
# 1        Bob
# 2    Charlie
# 3      David

# Multiple columns using loc
print("\nUsing loc - Columns 'Name' and 'City':")
print(df.loc[:, ["Name", "City"]])

# OUTPUT:
#       Name     City
# 0    Alice    Delhi
# 1      Bob   Mumbai
# 2  Charlie  Chennai
# 3    David     Pune

# Multiple columns using iloc
print("\nUsing iloc - Column index 0 and 2:")
print(df.iloc[:, [0, 2]])

# OUTPUT:
#       Name     City
# 0    Alice    Delhi
# 1      Bob   Mumbai
# 2  Charlie  Chennai
# 3    David     Pune
print("-" * 60)


# ============================================================
# 3. EXTRACTING PARTICULAR CELL DATA
# ============================================================
print("\n3. Extracting Particular Cell Data")
print("-------------------------------------")

# loc: select cell using row label and column name
print("\nUsing loc - Cell at row 1, column 'City':")
print(df.loc[1, "City"])

# OUTPUT:
# Mumbai

# iloc: select cell using row index and column position
print("\nUsing iloc - Cell at row index 1, column index 2:")
print(df.iloc[1, 2])

# OUTPUT:
# Mumbai

# loc selecting a range of cells
print("\nUsing loc - Rows 0 to 2, Columns 'Name' to 'City':")
print(df.loc[0:2, "Name":"City"])

# OUTPUT:
#       Name   Age     City
# 0    Alice   25     Delhi
# 1      Bob   30    Mumbai
# 2  Charlie   35   Chennai

# iloc selecting cells by numeric slicing
print("\nUsing iloc - Rows 0 to 2, Columns 0 to 2:")
print(df.iloc[0:3, 0:3])

# OUTPUT:
#       Name   Age     City
# 0    Alice   25     Delhi
# 1      Bob   30    Mumbai
# 2  Charlie   35   Chennai

print("\n--- END OF PROGRAM ---")
