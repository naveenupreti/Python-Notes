# -------------------------------
# 2D Lists (Matrix Addition)
# -------------------------------

A = [
     [1, 2],
     [3, 4]
    ]

B = [
     [5, 6],
     [7, 8]
    ]

# Get dimensions
rows = len(A)
cols = len(A[0])

# Initialize result matrix
result = []
for i in range(rows):
    new_row = []
    for j in range(cols):
        sum_value = A[i][j] + B[i][j]
        new_row.append(sum_value)
    result.append(new_row)

# Print the result with indices
print("Resultant Matrix (A + B) with indices:")
for i in range(rows):
    for j in range(cols):
        print(f"result[{i}][{j}] = {result[i][j]}", end="\t")
    print()
    
'''
Output
Resultant Matrix (A + B) with indices:
result[0][0] = 6	result[0][1] = 8	
result[1][0] = 10	result[1][1] = 12
'''
