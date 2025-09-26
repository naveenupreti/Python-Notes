
#Lists - Python Examples

# -------------------------------
# 1. Creating and Printing Lists
# -------------------------------

# Creating a simple list of numbers
nums = [10, 20, 30, 40]
print(nums)  # Output: [10, 20, 30, 40]

# List can contain mixed data types (string, int, float, bool)
mixed = ["A", 100, 3.14, True]
print(mixed)  # Output: ['A', 100, 3.14, True]

# Nested list (list inside another list)
nested = [1, 2, [3, 4], 5]
print(nested)  # Output: [1, 2, [3, 4], 5]


# -------------------------------
# 2. Accessing and Modifying Lists
# -------------------------------

# Indexing starts from 0 (like strings)
print(nums[0])   # First element → 10
print(nums[-1])  # Last element → 40

# Lists are mutable → elements can be changed
nums[1] = 25
print(nums)  # [10, 25, 30, 40]


# -------------------------------
# 3. List Slicing
# -------------------------------

# Extracting sub-lists using slice
print(nums[1:3])   # From index 1 to 2 → [25, 30]
print(nums[:2])    # From beginning → [10, 25]
print(nums[2:])    # From index 2 onwards → [30, 40]
print(nums[::-1])  # Reversed list → [40, 30, 25, 10]


# -------------------------------
# 4. List Methods
# -------------------------------

fruits = ["apple", "banana", "cherry"]

# Append adds a new element at the end
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

# Insert element at index
fruits.insert(1, "kiwi")
print(fruits)  # ['apple', 'kiwi', 'banana', 'cherry', 'orange']

# Remove by value
fruits.remove("banana")
print(fruits)  # ['apple', 'kiwi', 'cherry', 'orange']

# Pop removes by index (default last element)
popped = fruits.pop()
print(popped)   # 'orange'
print(fruits)   # ['apple', 'kiwi', 'cherry']

# Extend merges another list
fruits.extend(["grapes", "melon"])
print(fruits)  # ['apple', 'kiwi', 'cherry', 'grapes', 'melon']

# Count occurrences
print(fruits.count("apple"))  # 1

# Sorting
fruits.sort()
print(fruits)  # ['apple', 'cherry', 'grapes', 'kiwi', 'melon']

# Reverse order
fruits.reverse()
print(fruits)  # ['melon', 'kiwi', 'grapes', 'cherry', 'apple']


# -------------------------------
# Traversing a List
# -------------------------------

animals = ["dog", "cat", "lion", "tiger"]

# Using for loop
for animal in animals:
    print(animal)

# Using while loop
i = 0
while i < len(animals):
    print(animals[i])
    i += 1


# -------------------------------
# Sorting a List
# -------------------------------

numbers = [15, 3, 9, 1, 12]

# Ascending order
numbers.sort()
print(numbers)  # [1, 3, 9, 12, 15]

# Descending order
numbers.sort(reverse=True)
print(numbers)  # [15, 12, 9, 3, 1]

'''
1️sort() vs sorted()

| Feature           | `sort()`                      | `sorted()`                                                  |
| ----------------- | ----------------------------- | ----------------------------------------------------------- |
| **Type**          | Method of a list              | Built-in function                                           |
| **Original list** | Changes the list **in-place** | Returns a **new sorted list**, original list stays the same |
| **Return value**  | `None`                        | New list                                                    |
| **Works on**      | Only lists                    | Any iterable (list, tuple, string, etc.)                    |

'''
#Example with sort() (in-place):

numbers = [4, 1, 7, 3]
numbers.sort()        # Sorts the list itself
print(numbers)        # Output: [1, 3, 4, 7]


#Example with sorted() (returns new list):

numbers = [4, 1, 7, 3]
new_numbers = sorted(numbers)   # Returns a new sorted list
print(new_numbers)              # [1, 3, 4, 7]
print(numbers)                  # Original list unchanged: [4, 1, 7, 3]


'''
2️reverse() vs reversed()
| Feature           | `reverse()`                    | `reversed()`                                                            |
| ----------------- | ------------------------------ | ----------------------------------------------------------------------- |
| **Type**          | Method of a list               | Built-in function                                                       |
| **Original list** | Reverses the list **in-place** | Returns an **iterator** that goes through the elements in reverse order |
| **Return value**  | `None`                         | Iterator (can convert to list using `list()`)                           |
| **Works on**      | Only lists                     | Any iterable                                                            |

'''
#Example with reverse() (in-place):

numbers = [1, 2, 3, 4]
numbers.reverse()     # Reverse the list itself
print(numbers)        # Output: [4, 3, 2, 1]


#Example with reversed() (returns iterator):

numbers = [1, 2, 3, 4]
rev_numbers = reversed(numbers)   # Returns an iterator
print(list(rev_numbers))          # Convert to list: [4, 3, 2, 1]
print(numbers)                    # Original list unchanged: [1, 2, 3, 4]

'''
Quick summary:

sort() → sorts in-place, only lists.

sorted() → returns a new sorted list, works on any iterable.

reverse() → reverses in-place, only lists.

reversed() → returns an iterator in reverse order, works on any iterable.
'''

# -------------------------------
# Copying and Cloning Lists
# -------------------------------

original = [1, 2, 3]
shallow_copy = original  # Both refer to same list
clone = original[:]      # Creates new list (clone)

original.append(4)

print(shallow_copy)  # [1, 2, 3, 4]
print(clone)        # [1, 2, 3]


# -------------------------------
# List Comprehensions
# -------------------------------
'''
What is a list comprehension?

A list comprehension is a compact way to create a list in Python using a single line of code, instead of writing multiple lines with loops.

General form:

[ expression for item in iterable if condition ]


expression → what each item in the new list should be

item in iterable → loops over each element in the original collection

if condition → optional, filters elements

Simple Example 1: Squares of numbers

Instead of writing:
'''
# Generate a list of squares
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)

#We can use list comprehension:
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

'''
One line does the same thing as three lines with a loop.

Simple Example 2: Even numbers

Using a normal loop:
'''
# Generate a list of Even numbers
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)
print(evens)  # Output: [0, 2, 4, 6, 8]

#With list comprehension:
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# -------------------------------
# Exercise A – Prime Numbers in a List
# -------------------------------

# Check if a number is prime
def is_prime(n):
    """Return True if n is prime, else False."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Generate a list of prime numbers between 1 and 50
prime_list = [x for x in range(1, 51) if is_prime(x)]
print(prime_list)

'''
This line is a list comprehension, which is a compact way to create lists. Let’s break it down:

prime_list = [x for x in range(1, 51) if is_prime(x)]
range(1, 51) → generates numbers from 1 to 50.

if is_prime(x) → keeps only numbers x that are prime.

[x ...] → creates a list of those numbers.
'''

# Generate a list of prime numbers between 1 and 50
prime_list = []
for x in range(1, 51):
    if is_prime(x):
        prime_list.append(x)

print(prime_list)


# -------------------------------
# Exercise B – Find Second Largest Number
# -------------------------------

nums = [12, 45, 32, 67, 89, 21]

# Sort and pick the second largest
nums_sorted = sorted(nums, reverse=True)
second_largest = nums_sorted[1]
print("Second largest:", second_largest)


# -------------------------------
# Exercise C – Reverse Words in a Sentence
# -------------------------------

sentence = "Python makes programming fun"

# Split into words, reverse list, join back
reversed_sentence = " ".join(sentence.split()[::-1])
print(reversed_sentence)  # fun programming makes Python


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




