# -------------------------------------------------------------
# Program: Important pandas functions with explanations + OUTPUT
# -------------------------------------------------------------
import pandas as pd

# --------------------------
# Create a Series
# --------------------------
s = pd.Series([10, 20, 30, 40])
print("Series:\n", s)

# head() – first n rows
print("\nHead (2 rows):\n", s.head(2))

# tail() – last n rows
print("\nTail (2 rows):\n", s.tail(2))

# index and values
print("\nIndex:", s.index)
print("Values:", s.values)

# describe() – summary statistics
print("\nDescribe:\n", s.describe())

# mean(), sum(), max(), min()
print("\nMean:", s.mean())
print("Sum:", s.sum())
print("Max:", s.max())
print("Min:", s.min())

# -------------------------------------------------------------
# DataFrame operations
# -------------------------------------------------------------
df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Marks": [85, 90, 75]
})

print("\nDataFrame:\n", df)

# info()
print("\nDataFrame info():")
print(df.info())

# describe()
print("\nDescribe DataFrame:\n", df.describe())

# loc and iloc
print("\nloc[0]:\n", df.loc[0])
print("\niloc[1]:\n", df.iloc[1])

# Add new column
df["Total"] = df["Marks"] + 5
print("\nAdded 'Total' column:\n", df)

# Drop column
df2 = df.drop("Total", axis=1)
print("\nDropped 'Total' column:\n", df2)

# Rename column
df3 = df.rename(columns={"Marks": "Score"})
print("\nRenamed 'Marks' to 'Score':\n", df3)

# Filter
print("\nRows where Marks > 80:\n", df[df["Marks"] > 80])

# Sorting
print("\nSorted by Marks:\n", df.sort_values("Marks"))


# -------------------------------------------------------------
# SAMPLE OUTPUT (Will vary slightly due to memory info)
# -------------------------------------------------------------
"""
Series:
 0    10
 1    20
 2    30
 3    40
 dtype: int64

Head (2 rows):
 0    10
 1    20

Tail (2 rows):
 2    30
 3    40

Index: RangeIndex(start=0, stop=4, step=1)
Values: [10 20 30 40]

Describe:
 count     4.000000
 mean     25.000000
 std      12.909944
 min      10.000000
 max      40.000000

Mean: 25.0
Sum: 100
Max: 40
Min: 10

DataFrame:
   Name  Marks
0    A     85
1    B     90
2    C     75

loc[0]:
 Name       A
 Marks     85

iloc[1]:
 Name       B
 Marks     90

Added 'Total' column:
   Name  Marks  Total
0    A     85     90
1    B     90     95
2    C     75     80

Dropped 'Total' column:
   Name  Marks
0    A     85
1    B     90
2    C     75

Renamed 'Marks' to 'Score':
   Name  Score
0    A     85
1    B     90
2    C     75

Rows where Marks > 80:
   Name  Marks  Total
0    A     85     90
1    B     90     95

Sorted by Marks:
   Name  Marks  Total
2    C     75     80
0    A     85     90
1    B     90     95
"""
