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
# 5. List Comprehensions
# -------------------------------

# Generate a list of squares
squares = [x ** 2 for x in range(6)]
print(squares)  # [0, 1, 4, 9, 16, 25]

# Filtering list comprehension
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]


# -------------------------------
# 6. Nested Lists and Matrix
# -------------------------------

# Representing a matrix as a list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 2, column 3
print(matrix[1][2])  # 6

# Transpose matrix using list comprehension
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


# -------------------------------
# Problem 8.1 – Basic List Operations
# -------------------------------

students = ["Ajay", "Amit", "Anita", "Amol", "Arun"]
print(students)

# Insert new student
students.insert(2, "Anil")
print(students)

# Append at the end
students.append("Avinash")
print(students)

# Delete element
students.remove("Amol")
print(students)

# Replace element
students[0] = "Ajinkya"
print(students)


# -------------------------------
# Problem 8.2 – List with Mixed Data Types
# -------------------------------

mixed_data = [100, "Python", 3.14, [10, 20], True]
print(mixed_data)


# -------------------------------
# Problem 8.3 – Traversing a List
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
# Problem 8.4 – Copying and Cloning Lists
# -------------------------------

original = [1, 2, 3]
shallow_copy = original  # Both refer to same list
clone = original[:]      # Creates new list (clone)

original.append(4)

print(shallow_copy)  # [1, 2, 3, 4]
print(clone)        # [1, 2, 3]


# -------------------------------
# Problem 8.5 – 2D Lists (Matrix Addition)
# -------------------------------

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Adding two matrices
result = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
print(result)  # [[6, 8], [10, 12]]


# -------------------------------
# Problem 8.6 – Sorting a List
# -------------------------------

numbers = [15, 3, 9, 1, 12]

# Ascending order
numbers.sort()
print(numbers)  # [1, 3, 9, 12, 15]

# Descending order
numbers.sort(reverse=True)
print(numbers)  # [15, 12, 9, 3, 1]


# =========================================================
# EXTRA EXERCISES (A, B, C)
# =========================================================

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
