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
"""
================ INSTALLATION COMMANDS =================
# Install NumPy on Q4OS Linux:
# sudo apt install python3-numpy

# Install NumPy, Pandas, Matplotlib, SciPy, Seaborn on Q4OS Linux:
# sudo apt update && sudo apt install python3-numpy python3-pandas python3-matplotlib python3-scipy python3-seaborn

# Install NumPy on Windows:
# pip install numpy
"""

"""
================ DATA SCIENCE OVERVIEW =================
- Data Science: Collecting, storing, analyzing, interpreting data to extract insights.
- Combines:
    * Statistics & Mathematics
    * Programming (Python, R)
    * Data Analysis & Visualization
    * Machine Learning & AI
- Difference from Data Analytics:
    * Analytics: Understanding past/current trends
    * Data Science: Predicting future trends, building models
- Importance: Better decisions, accurate predictions, automation, reducing costs/risks
- Real-life examples: Netflix recommendations, Amazon suggestions, Fraud detection, Traffic prediction, Disease prediction
- Key Steps: Data Collection → Cleaning → Analysis → Visualization → Model Building → Deployment
- Technologies: Python, R, SQL, NumPy, Pandas, Matplotlib, Scikit-learn, TensorFlow, PyTorch
"""

import numpy as np

print("\n================ SIZE OF NUMPY DATA TYPES =================")
print(f"Size of np.int32: {np.int32().itemsize} bytes")  # Output: 4 bytes
print(f"Size of np.int64: {np.int64().itemsize} bytes")  # Output: 8 bytes
print(f"Size of np.float32: {np.float32().itemsize} bytes")  # Output: 4 bytes
print(f"Size of np.float64: {np.float64().itemsize} bytes")  # Output: 8 bytes

# ---------------- 1D ARRAY ----------------
arr1 = np.array([10, 20, 30, 40, 50])
print("\n=== 1D ARRAY DETAILS ===")
print("Array:", arr1)  # Output: [10 20 30 40 50]
print("Type of elements (dtype):", arr1.dtype)  # Output: int64
print("Number of elements (size):", arr1.size)  # Output: 5
print("Memory address of first element (ctypes.data):", arr1.ctypes.data)  # Output: <address>
print("Total bytes occupied (nbytes):", arr1.nbytes)  # Output: 40

# ---------------- 2D ARRAY ----------------
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n=== 2D ARRAY DETAILS ===")
print("Array:\n", arr2)
# Output:
# [[1 2 3]
#  [4 5 6]]
print("Type of elements:", arr2.dtype)  # Output: int64
print("Number of elements:", arr2.size)  # Output: 6
print("Base address:", arr2.ctypes.data)  # Output: <address>
print("Bytes occupied:", arr2.nbytes)  # Output: 48

# ---------------- 1D ARRAY OPERATIONS ----------------
arr1_ops = np.array([25, 5, 40, 15, 10])
print("\n=== 1D ARRAY OPERATIONS ===")
print("Array:", arr1_ops)  # Output: [25  5 40 15 10]
print("Sorted array (np.sort):", np.sort(arr1_ops))  # Output: [ 5 10 15 25 40]
print("Maximum (np.max):", np.max(arr1_ops))  # Output: 40
print("Minimum (np.min):", np.min(arr1_ops))  # Output: 5
print("Sum of elements (np.sum):", np.sum(arr1_ops))  # Output: 95
print("Mean of elements (np.mean):", np.mean(arr1_ops))  # Output: 19.0

# ---------------- 2D ARRAY OPERATIONS ----------------
arr2_ops = np.array([[30, 20, 10],
                     [40, 60, 50],
                     [90, 80, 70]])
print("\n=== 2D ARRAY OPERATIONS ===")
print("Array:\n", arr2_ops)
# Output:
# [[30 20 10]
#  [40 60 50]
#  [90 80 70]]
print("Row-wise sorted (np.sort with axis=1):\n", np.sort(arr2_ops, axis=1))
# Output:
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]
print("Maximum:", np.max(arr2_ops))  # Output: 90
print("Minimum:", np.min(arr2_ops))  # Output: 10
print("Sum:", np.sum(arr2_ops))  # Output: 450
print("Mean:", np.mean(arr2_ops))  # Output: 50.0
print("Row-wise Max (axis=1):", np.max(arr2_ops, axis=1))  # Output: [30 60 90]
print("Row-wise Min:", np.min(arr2_ops, axis=1))  # Output: [10 40 70]
print("Row-wise Sum:", np.sum(arr2_ops, axis=1))  # Output: [60 150 240]
print("Row-wise Mean:", np.mean(arr2_ops, axis=1))  # Output: [20. 50. 80.]
print("Column-wise Max (axis=0):", np.max(arr2_ops, axis=0))  # Output: [90 80 70]
print("Column-wise Min:", np.min(arr2_ops, axis=0))  # Output: [30 20 10]
print("Column-wise Sum:", np.sum(arr2_ops, axis=0))  # Output: [160 160 130]
print("Column-wise Mean:", np.mean(arr2_ops, axis=0))  # Output: [53.33333333 53.33333333 43.33333333]

# ---------------- ARRAY DIMENSIONS, SHAPE, TRANSPOSE ----------------
arr_dim = np.array([[10, 20, 30],
                    [40, 50, 60]])
print("\n=== ARRAY DIMENSIONS & TRANSPOSE ===")
print("Original Array:\n", arr_dim)
# Output:
# [[10 20 30]
#  [40 50 60]]
print("Dimensions (ndim):", arr_dim.ndim)  # Output: 2
print("Shape (rows x cols):", arr_dim.shape)  # Output: (2, 3)
print("Total elements (size):", arr_dim.size)  # Output: 6
transpose_arr = arr_dim.T
print("Transpose of array:\n", transpose_arr)
# Output:
# [[10 40]
#  [20 50]
#  [30 60]]

# ---------------- MATRIX MULTIPLICATION ----------------
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8],[9,10],[11,12]])
print("\nMatrix A:\n", A)
# Output:
# [[1 2 3]
#  [4 5 6]]
print("Shape of A:", A.shape)  # Output: (2, 3)
print("Matrix B:\n", B)
# Output:
# [[ 7  8]
#  [ 9 10]
#  [11 12]]
print("Shape of B:", B.shape)  # Output: (3, 2)
if A.shape[1] == B.shape[0]:
    C = np.matmul(A,B)  # this may also be used C = A @ B for Matrix multiplication
    print("Result of A x B:\n", C)
    # Output:
    # [[ 58  64]
    #  [139 154]]
else:
    print("Matrices not compatible for multiplication")

# ---------------- ARRAY CREATION AND INDEXING ----------------
natural = np.arange(1,11)
even = np.arange(2,21,2)
arr_idx = np.array([5,10,15,20,25,30])
print("\nFirst 10 natural numbers:", natural)  # Output: [ 1  2  3  4  5  6  7  8  9 10]
print("First 10 even numbers:", even)  # Output: [ 2  4  6  8 10 12 14 16 18 20]
print("First element arr_idx[0]:", arr_idx[0])  # Output: 5
print("Slice arr_idx[1:4]:", arr_idx[1:4])  # Output: [10 15 20]
print("Last element arr_idx[-1]:", arr_idx[-1])  # Output: 30

# ---------------- RESHAPE & FLATTEN ----------------
arr3 = np.arange(1,13)
reshaped = arr3.reshape(3,4)
flat = reshaped.flatten()
print("\nOriginal 1D array:", arr3)  # Output: [ 1  2  3  4  5  6  7  8  9 10 11 12]
print("Reshaped (3x4):\n", reshaped)
# Output:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
print("Flattened:", flat)  # Output: [ 1  2  3  4  5  6  7  8  9 10 11 12]
print("arr3[2:5] =", arr3[2:5])  # Output: [3 4 5]
print("arr3[:-4] =", arr3[:-4])  # Output: [ 1  2  3  4  5  6  7  8]

# ---------------- FIRST 10 PRIME NUMBERS ----------------
def is_prime(n):
    """Check if n is prime"""
    if n < 2:
        return False
    for i in range(2,int(np.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

primes = []
num = 2
while len(primes)<10:
    if is_prime(num):
        primes.append(num)
    num +=1
primes = np.array(primes)
print("\nFirst 10 prime numbers:", primes)  # Output: [ 2  3  5  7 11 13 17 19 23 29]
