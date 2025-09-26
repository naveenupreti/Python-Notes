# Representing a matrix as a list of lists (nested lists)
matrix = [
    [1, 2], 
    [3, 4],
    [5, 6], 
    [7, 8]
]

rows = len(matrix)
cols = len(matrix[0])

# Print the original matrix with indices
print("Original Matrix with indices:")
for i in range(rows):
    for j in range(cols):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}", end="\t")
    print()  # new line after each row

# Transpose the matrix dynamically
transpose = []
for i in range(cols):          # iterate over columns
    new_row = []
    for j in range(rows):      # iterate over rows
        new_row.append(matrix[j][i])
    transpose.append(new_row)

# Print the transposed matrix with indices
print("\nTransposed Matrix with indices:")
for i in range(len(transpose)):
    for j in range(len(transpose[0])):
        print(f"transpose[{i}][{j}] = {transpose[i][j]}", end="\t")
    print()

# Note about Python's memory layout
print("\nNote: Python lists are stored as objects, not as fixed-size arrays.")
print("So Python does not enforce row-major or column-major storage like C/Fortran.")
print("However, when using NumPy, arrays are row-major by default (C-order).")

'''
Output:
Original Matrix with indices:
matrix[0][0] = 1	matrix[0][1] = 2	
matrix[1][0] = 3	matrix[1][1] = 4	
matrix[2][0] = 5	matrix[2][1] = 6	
matrix[3][0] = 7	matrix[3][1] = 8	

Transposed Matrix with indices:
transpose[0][0] = 1	transpose[0][1] = 3	transpose[0][2] = 5	transpose[0][3] = 7	
transpose[1][0] = 2	transpose[1][1] = 4	transpose[1][2] = 6	transpose[1][3] = 8	

Note: Python lists are stored as objects, not as fixed-size arrays.
So Python does not enforce row-major or column-major storage like C/Fortran.
However, when using NumPy, arrays are row-major by default (C-order).
'''