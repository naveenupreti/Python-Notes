'''
Run the following command to install numpy on Q4OS linux
sudo apt install python3-numpy

Run the following command to install numpy,pandas,matplotlib,scipy, seaborn on Q4OS linux
sudo apt update && sudo apt install python3-numpy python3-pandas python3-matplotlib python3-scipy python3-seaborn

Run the following command to install numpy on windows
pip install numpy
'''
'''
What is Data Science?
Data Science is the field that deals with collecting, storing,
analyzing, and interpreting data to extract useful information,
patterns, and insights that help in decision-making.

Data Science is the interdisciplinary field that uses statistical methods,
algorithms, and computing tools to extract meaningful insights and knowledge from data.

It combines:

Statistics & Mathematics
Programming (Python, R)
Data Analysis & Visualization
Machine Learning & AI
Domain Knowledge

In short:

👉 Data Science = Data + Algorithms + Business Understanding

Data Science is a broad field that uses statistics, programming, machine learning,
and algorithms to extract insights and make predictions from large datasets.

Data Analytics is a subset of Data Science that focuses on analyzing current or historical
data to understand trends, patterns, and support business decisions.

Example
Data Analytics:
A company wants to know why sales dropped last month.

Data Science:
A company wants to predict next month’s sales.


✅ Why is Data Science important?

Because companies generate huge amounts of data and need:
Better decisions
Accurate predictions
Automation
Understanding customer behaviour
Reducing costs and risks

✅ Real-Life Examples of Data Science
Netflix recommending movies
Amazon suggesting products
Banks detecting fraud
Google Maps predicting traffic
Healthcare predicting diseases

✅ Key Steps in Data Science
    Data Collection
    Data Cleaning
    Data Analysis
    Data Visualization
    Model Building (ML)
    Deployment & Monitoring

✅ Technologies Used in Data Science

Python, R, SQL
NumPy, Pandas, Matplotlib
Scikit-Learn, TensorFlow, PyTorch
Big Data tools (Hadoop, Spark)


What is NumPy?
NumPy (Numerical Python) is a powerful Python library used for:
numerical computing
working with arrays (especially multi-dimensional arrays)
performing mathematical, scientific, and statistical operations efficiently
It is one of the foundation libraries for Data Science, Machine Learning, AI,
Scientific Computing, and Engineering applications.

Why do we use NumPy?

1. Fast and Efficient

NumPy arrays are stored in continuous memory blocks and use optimized C code internally.
→ This makes them much faster than Python lists for numerical operations.

Example:
Performing operations on a 1 lakh element list vs a NumPy array —
NumPy is 50–100 times faster.

2. Supports Multi-Dimensional Arrays

Python lists are one-dimensional (lists inside lists become slow).
NumPy supports:

1D arrays → vectors
2D arrays → matrices
ND arrays → tensors

Useful in scientific and machine learning applications.

3. Rich Mathematical Functions

NumPy provides hundreds of built-in functions:

trigonometric (sin, cos, tan)

logarithmic (log, log10)

statistical (mean, median, std)

algebra (dot, inv, transpose)

random number generation

These make complex calculations easy and very fast.

4. Vectorization (No Need for Loops)

With NumPy, you can perform an entire operation on an array without writing loops.

Example:

import numpy as np
a = np.array([1,2,3])
b = a * 10
print(b)


Output:

[10 20 30]


This is cleaner, faster, and less error-prone.

5. Backbone of Data Science Ecosystem

Libraries like:

Pandas

Scikit-learn

SciPy

TensorFlow

PyTorch

Matplotlib

are all built on top of NumPy arrays.

So learning NumPy is essential.

6. Memory Efficient

NumPy uses homogeneous data types (all elements have the same type),
allowing compact storage and efficient operations.

✅ In Short

NumPy is used because it makes numerical computing faster, easier,
and more efficient than using normal Python lists.
'''
import numpy as np

# Size of specific NumPy integer types
print(f"Size of np.int32: {np.int32().itemsize} bytes")
print(f"Size of np.int64: {np.int64().itemsize} bytes")
print(f"Size of np.float32: {np.float32().itemsize} bytes")
print(f"Size of np.float64: {np.float64().itemsize} bytes")
# ---- 1D Array ----
arr1 = np.array([10, 20, 30, 40, 50])

print("=== 1D ARRAY DETAILS ===")
print("Array:", arr1)
print("Type of elements (dtype):", arr1.dtype)
print("Number of elements:", arr1.size)
print("Base address:", arr1.ctypes.data)
print("Bytes occupied:", arr1.nbytes)


# ---- 2D Array ----
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("\n=== 2D ARRAY DETAILS ===")
print("Array:\n", arr2)
print("Type of elements (dtype):", arr2.dtype)
print("Number of elements:", arr2.size)
print("Base address:", arr2.ctypes.data)
print("Bytes occupied:", arr2.nbytes)


import numpy as np
# ------------------ 1D ARRAY ------------------
arr1 = np.array([25, 5, 40, 15, 10])

print("=== 1D ARRAY OPERATIONS ===")
print("Array:", arr1)

print("Sorted:", np.sort(arr1))
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))


# ------------------ 2D ARRAY ------------------
arr2 = np.array([[30, 20, 10],
                 [40, 60, 50],
                 [90, 80, 70]])

print("\n=== 2D ARRAY OPERATIONS ===")
print("Array:\n", arr2)

# Sorting (note: sorted row-wise)
print("Sorted (row-wise):\n", np.sort(arr2))
print("Maximum:", np.max(arr2))
print("Minimum:", np.min(arr2))
print("Sum:", np.sum(arr2))
print("Mean:", np.mean(arr2))

# Row-wise operations.axis=1 is for row-wise
print("\nRow-wise Max:", np.max(arr2, axis=1))
print("Row-wise Min:", np.min(arr2, axis=1))
print("Row-wise Sum:", np.sum(arr2, axis=1))
print("Row-wise Mean:", np.mean(arr2, axis=1))

# Column-wise operations.axis=0 is for column-wise
print("\nColumn-wise Max:", np.max(arr2, axis=0))
print("Column-wise Min:", np.min(arr2, axis=0))
print("Column-wise Sum:", np.sum(arr2, axis=0))
print("Column-wise Mean:", np.mean(arr2, axis=0))


import numpy as np
print("=== NUMPY ARRAY OPERATIONS ===\n")
# -------- 1. Dimensions of a NumPy Array --------
arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print("Original Array:\n", arr)
print("Dimensions of array:", arr.ndim)
print("Shape of array:", arr.shape)   # rows, columns
print("Size (total elements):", arr.size)

# -------- 2. Transpose of a Matrix --------

transpose_arr = arr.T
print("\nTranspose of Matrix:\n", transpose_arr)

# -------- 3. Matrix Multiplication with Compatibility Check --------

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("\nMatrix A:\n", A)
print("Shape of A:", A.shape)

print("\nMatrix B:\n", B)
print("Shape of B:", B.shape)

# Compatibility check: columns(A) == rows(B)
if A.shape[1] == B.shape[0]:
    C = np.matmul(A, B)   # or A @ B
    print("\nMatrices are compatible!")
    print("Result of A x B:\n", C)
else:
    print("\nMatrices are NOT compatible for multiplication.")
    print("Condition failed: Columns of A != Rows of B")



import numpy as np

natural = np.arange(1, 11)
print("First 10 natural numbers:", natural)

even = np.arange(2, 21, 2)
print("First 10 even numbers:", even)

arr = np.array([5, 10, 15, 20, 25, 30])
print(arr[0])        # first element
print(arr[1:4])      # slice from index 1 to 3
print(arr[-1])       # last element



import numpy as np
arr = np.arange(1, 13)   # 1 to 12
print(arr)
reshaped = arr.reshape(3, 4)
flat = reshaped.flatten()

print("Reshaped:\n", reshaped)
print("Flattened:", flat)
print("arr[2:5]=",arr[2:5])
print("arr[:-4]=",arr[:-4])



import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Collect first 10 primes
primes = []
num = 2
while len(primes) < 10:
    if is_prime(num):
        primes.append(num)
    num += 1

primes = np.array(primes)
print("First 10 prime numbers:", primes)


